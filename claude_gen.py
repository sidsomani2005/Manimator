import vertexai
from vertexai.generative_models import GenerativeModel
import os
from dotenv import load_dotenv
import json
from imagen import main
load_dotenv()
import copy
from anthropic import AnthropicVertex
import anthropic


vertexai.init(project=os.getenv("PROJECT_ID"), location="us-central1")
client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=os.getenv("ANTHROPIC_API")
)

def steps_agent(prompt: str):
    system_instruction = """

        
    You are an assistant that generates SPECIFIC instructions for an animation that explains a particular concept and returns JSON response consisting of "titles", "images", "srt", and "info" fields.

    - The "title" field is a short title of the concept you are making the animation for. (eg Addition, Subtraction, EigenValues) Be super concise and direct.
    - The "images" field is a dictionary with keys being names of objects used in the explanation and values being null.
    - The "info" field is a dictionary with keys being the timestamps for the voiceover and values being steps on how to draw and animate the concept being explained at that timestamp. Adhere to mathematical logic and physics. 
      If there are no concepts being explained at a timestamp, then the value should be an empty string. USE AS MANY STEPS AS YOU NEED. 
    - The "srt" field is a transcript in an SRT format for a one-person voiceover with timestamps explaining the concept.

   
      

    Your task is to take the user's prompt and generate a JSON response as per the format above.
    When it comes to deciding the images, if you believe the overall task is complicated assign all the values as "Manim", else use daily objects and keep the value as null.

    Here is a sample of the format you should output in:
    {
        "title": "<Add Title>",
        "images": {
            "<Any Item>": null
            <more as needed>,
        },
        "srt": {
        <Add SRT>
        },
        "info":{
            "<timestamp1>":<Action>,
            <more as needed>,
        }
        
    }
    MAKE SURE YOU OUTPUT A VALID JSON

    """

    message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    system=system_instruction,
    messages=[
        {"role": "user", "content": prompt}
    ]
    ),
   

    return message[0].content[0].text

def steps_checking_agent(prompt: str):
    system_instruction = """
    You are super reader that checks the work of another agent. You will be given a json input of the form below and output a similar JSON with some changes: 
    {
        "images": {
            "<Any Item>": null
            <more as present>,
        },
        "info":{
            "<timestamp1>":<Action>,
            <more as present>,
        }
        
    }


    Your job is to check the images and info dictionaries in the following order:
        1) If you find any key in the images dictionary that SAID as a mathematical shape (arrow, circle, square) replace their value with "Manim". DO NOT ADD ANY IMAGES TO THE DICTIONARY
        2) After all checks for the image dictionary are completed you will go to the info dictionary and see where the any of the objects which are keys in the images dictionary are being used. Once found replace them with *_<objectkey>_* where objectkey is the actual key from the images dictionary.

    You will then return the updated json.

    """
    model = GenerativeModel(
        model_name="gemini-1.5-pro", system_instruction=system_instruction
    )


    response = model.generate_content(prompt)
    return response.text


def load_references():
    with open("reference_db.md", "r") as f:  
        references = f.read()
    return references


def manimator(data: str):
    system_instruction = """
    You are professional at Manim (0.18.1) a python library used to make animations. 
    You have the entire manim library at your disposal. Feel free to check the internet manim documentation: https://docs.manim.community/en/stable/ for any confusion you might have.

    **Your Task:**

    - **Input:** You will receive a JSON object with three fields: 'title', 'images', and 'steps'
    - The 'title' field is a short title of the concept you are making the animation for. (eg Addition, Subtraction, EigenValues) Be super concise and direct.
    - The 'images' field is a dictionary with keys being names of daily object used in the explanation (e.g., 'apple', 'banana') and values are either the GCP link to the image or the word "Manim".
    - The 'srt' field is a transcript in an SRT format for a one-person voiceover with timestamps explaining the concept. 
    - The 'info' field is a dictionary with keys being the timestamps from the generated SRT file and values being detailed steps on how to draw and animate the concept being explained at that timestamp. For example, when explaining projectile motion,
      there could be a step to draw a ball at the top of the screen and animate it moving downwards in a parabolic path. In your steps, use the images that were generated above. Adhere to mathematical logic and physics. If there are no concepts being explained at a timestamp, then the value should be an empty string.
    - A sample JSON file input would look like: 
    {
        "title": "<Title present>",
        "images": {
            "<Any Item>": null
            <more as present>,
        },
        "srt": {
        <given srt>
        },
        "info":{
            "<timestamp1>":<Action>,
            <more as present>,
        }
        
    }
    
    - **Output:** Generate Manim code that:
    - Generate Manim code that performs A SIMPLE animation detailed in info with a voiceover from the srt.
    - The code generated should provide an animation that sequentially depicts each step in chronological order. 
    - Incorporates the images provided in the `images` dictionary whenever they are mentioned in the text. You must SCALE THEM RELATIVELY SINCE THEY ARE ALL OF THE SAME SIZE.
    - If a image link is not provided, or is 'Manim', this means that the code can be generates directly from the manim library - MEANING THAT THE CODE FOR THIS SHAPE WILL NEED TO BE WRITTEN. (e.g, 'images' : { 'apple' : 'manim' } means that the image for an apple NEEDS TO BE WRITTEN IN MANIM CODE BY THE MODEL ITSELF)
    - When an object denoted by `_*object_name*_` appears in the transcript, display the corresponding image using the provided GCP bucket link.
    - Synchronizes the animations with the voiceover using Manim's VoiceOver feature.
   

    **Output Format:**
    - Provide the complete Manim Python code as plain text.
    - Do not include any explanations outside the code.
    - Do not include any stray characters.
    - Output in the format of a Python script that can be run in a Manim environment directly without any modifications.
    - An example is given below:
        from manim import *
        from manim_voiceover import VoiceoverScene
        from manim_voiceover.services.gtts import GTTSService


        class GTTSExample(VoiceoverScene):
            def construct(self):
                self.set_speech_service(GTTSService(lang="en", tld="com"))

                circle = Circle()
                square = Square().shift(2 * RIGHT)

                with self.voiceover(text="This circle is drawn as I speak.") as tracker:
                    self.play(Create(circle), run_time=tracker.duration)

                with self.voiceover(text="Let's shift it to the left 2 units.") as tracker:
                    self.play(circle.animate.shift(2 * LEFT), run_time=tracker.duration)

                with self.voiceover(text="Now, let's transform it into a square.") as tracker:
                    self.play(Transform(circle, square), run_time=tracker.duration)

                with self.voiceover(text="Thank you for watching."):
                    self.play(Uncreate(circle))

                self.wait()


    **CRITICAL GUIDELINES: MUST FOLLOW**
    - **DO NOT USE VGROUP**
    - **USE THE LATEST MANIM VERSION**
    - **TRY AND MINIMIZE REPITITION IN YOUR SPEECH**
    - **MAKE SURE THE CODE WORKS**
    - **DO NOT USE ANY IMAGES OTHER THAN THE ONES IN THE IMAGE DICTIONARY PROVIDED**
    - **DO NOT ADD ANY AUDIO OTHER THAN THE VOICEOVER**
    - **Color Code:** ENSURE THAT THE BACKGROUND IS ALWAYS WHITW AND THE TEXT IS ALWAYS BLACK.
    - **Sequence of image/text:** ensure that the text is of slightly smaller font size ALWAYS and NEVER overlaps with the other images. THIS IS EXTREMELY IMPORTANT - ESPECIALLY THE OVERLAP ISSUE.
    - **Object Sizing:** SCALE EACH IMAGE RELATIVELY SINCE THEY ARE OF THE SAME SIZE.
    - **Object Placement:** Make sure each object is placed properly relative to other objects and nothing overlaps.
    - **Mathematical Equations:** if mathematical or arithmetic equations are being written in text, POSITION THEM AWAY FROM OTHER OBJECTS AND KEEP THEM IN ONE HORIZONTAL LINE - ENSURE THAT THEY DONT TRAIL OFF THE END OF THE CANVAS.

   
    """


    message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=3000,
    system=system_instruction,
    messages=[
        {"role": "user", "content": data}
    ]
    ),

    # references = load_references()
    # response = model.generate_content([data, references])
    return message[0].content[0].text





def remove_code_block_markers(text, language='json'):
    """
    Removes Markdown code block markers from the given text.

    Args:
        text (str): The input string containing Markdown code block.
        language (str): The language specifier after the opening backticks.

    Returns:
        str: The cleaned string without code block markers.
    """
    lines = text.strip().split('\n')
    
    if lines and lines[0].startswith(f'```{language}'):
        lines = lines[1:] 
    else:
        print("Warning: The input does not start with the expected code block marker.")
    
    if lines and lines[-1].strip() == '```':
        lines = lines[:-1] 
    else:
        print("Warning: The input does not end with the expected code block marker.")
    
    cleaned_text = '\n'.join(lines)
    return cleaned_text


def final_flow(prompt):
    initial_check = steps_agent(prompt)
    print(initial_check)
    # next_check = remove_code_block_markers(initial_check, "json")
    step_json = json.loads(initial_check)
    clone_json = copy.deepcopy(step_json)
    del clone_json["srt"]
    del clone_json["title"]
    changed_images = steps_checking_agent(json.dumps(clone_json, indent=2))
    changed_images = remove_code_block_markers(changed_images, "json")
    changed_json = json.loads(changed_images)
    step_json["images"] = changed_json["images"]
    step_json["info"] = changed_json["info"]
    print(json.dumps(step_json))
    next_check = main(step_json)
    print(next_check)
    # print(final_json)
    code = (manimator(next_check))
    # print(next_check)
    return (code)


if __name__ == "__main__":
    print(final_flow("multiplication"))




# def checking_agent(video: str, subject: str, code: str):
#     video_file = Part.from_uri(
#     uri=video,
#     mime_type="video/mp4",
#     )
#     system_instruction = """
#     You are an assistant that checks a video explaing a key concept called"""+  subject +""". 
#     You are given the video and the manim code to generate the video. Your job is to correct the manim code so the video
#     is correct and as intended. You must make sure that the concept is explained properly. You will only return manim code 
#     in the same format it was given to you. Dont explain anything just return the code.
#     """
#     contents = [video_file, "The video is attached and here is the code used to generate the video:" + code]
#     model = GenerativeModel(
#         model_name="gemini-1.5-pro", system_instruction=system_instruction
#     )

#     response = model.generate_content(contents)
#     return response.text



# def audio_agent(prompt: str):
    
#     system_instruction = """
#     You are master trascriber assistant that generates beautiful and extremely cohesive and clear speech transcripts based on the steps provided:

#     **Your Task:**

#     - **Input:** You will receive a JSON object with three fields: 'title', 'images', and 'steps'
#     - The 'title' field is a high level description or overarching topic of what the prompt is asking for. (e.g., if the prompt/explanation describes adding 2 sets of fruits, say 3 green apples to 5 red apples, the title would be 'addition')
#     - The `images` field is a dictionary where the keys are names of daily objects (e.g., 'apple', 'banana'). DO NOT WORRY ABOUT THIS DICTIONARY.
#     - The 'steps' field is a dictionary where the keys are the specific steps to generate speech transcriptions on. HOWEVER, THE VALUES CORRESPONDING TO EACH STEP WILL BE NULL. THESE VALUES ARE WHAT YOU NEED TO FILL WITH SPEECH TRANSCRIPTIONS (REFER TO OUTPUT GUIDELINES)
#     - Here is a sample of what the input would be for you to generate speech additions:
#         {
#             "title": "Subtraction",
#             "images": {
#                 "cookie": "https://storage.googleapis.com/path_to_cookie_image.png"
#             },
#             "steps" : 
#             {
#                 "Step 1: Initialize a canvas of size 800x600 pixels." : null
#                 "Step 2: Set the size of each cookie to 40x40 pixels." : null
#                 "Step 3: Add 5 cookies horizontally, starting at coordinates (100, 300) with 50 pixel spacing between each cookie." : null
#                 "Step 4: Apply a fade-in effect lasting 0.5 seconds for all five cookies." : null
#                 "Step 5: Add a minus sign at coordinates (450, 300) with a size of 50x50 pixels." : null
#                 "Step 6: Add the number '5' at coordinates (300, 200) with a font size of 48px bold." : null
#                 "Step 7: Add the number '2' at coordinates (550, 200) with a font size of 48px bold." : null
#                 "Step 8: Move 2 cookies starting from the rightmost cookie upwards from (300, 300) to (300, 100) one after the other with 0.5 seconds delay between each cookie and a fade-out effect over 0.3 seconds.": null
#                 "Step 9: Apply a scale-in effect to the minus sign over 0.3 seconds." : null
#                 "Step 10: Add an equals sign at coordinates (450, 200) with a size of 50x50 pixels and apply a fade-in effect over 0.5 seconds." : null
#                 "Step 11: Add the number '3' at coordinates (450, 100) with a font size of 48px bold and apply a fade-in effect over 0.5 seconds." : null
#             }
#         }


#     **Output**: 
#     - Each step (key) in the 'steps' field has a corresponding value. This value is a transcript in speech format for a one-person voiceover with timestamps explaining a concept. Objects from the `images` dictionary used in the text are denoted by `_*object_name*_`. 
#     - The output should be a JSON response that is the same as the input but includes the speech transcriptions for each respective step.


#     Your JSON output will have these fields:
#     - The 'title' field is a short title of the concept you are making the animation for (given in the input).
#     - The 'images' field is a dictionary with keys being names of daily object used in the animation (e.g., 'football', 'apple') and values being null (given in the input).
#     - The 'steps' field is a dictionary with keys being each step you take to make animation (given in the input) and the corresponding speech transcriptions (intended output).
    
#     GUIDELINES FOR SPEECH OUTPUT GENERATION:
#     - Based on the title, which is the overarching concept of the explanation, build a framework/reference for the larger topic of the speech transcriptions in totality.
#     - When generating the SPEECH transcriptions, ensure that they are for each step in the 'steps' key field, and correspond and flow logically.
#     - When generating the SPEECH transcriptions, ensure that it does NOT mention pixels, or coordinates. THESE TRANSCRIPTIONS MUST EXPLAIN CONCEPTS AND TOPICS AT A HIGH LEVEL.
#     - Focus on generating SPEECH transcriptions that synthesizes each steps based on the provided title and explains the steps in a conceptual manner and in a way that is being asked for and is very easy to comprehend and understand.


#     Here is a sample output:
#     {
#         "title" : "Subtraction",
#         "images" : 
#         {
#             "cookie": "https://storage.googleapis.com/path_to_cookie_image.png"
#         },
#         "steps" : 
#         {
#             "Step 1: Initialize a canvas of size 800x600 pixels." : "Let's explore subtraction.",
#             "Step 2: Set the size of each cookie to 40x40 pixels." : "Imagine you have a plate with 5 cookies on it.",
#             "Step 3: Add 5 cookies horizontally, starting at coordinates (100, 300) with 50 pixel spacing between each cookie." : "Each cookie represents one item in our total count.",
#             "Step 4: Apply a fade-in effect lasting 0.5 seconds for all five cookies." : "Now, let’s say you eat 2 of these cookies. .",
#             "Step 5: Add a minus sign at coordinates (450, 300) with a size of 50x50 pixels." : "We’ll start by taking away 2 cookies from the plate..",
#             "Step 6: Add the number '5' at coordinates (300, 200) with a font size of 48px bold." : "As each cookie is removed, our total number of cookies decreases.",
#             "Step 7: Add the number '2' at coordinates (550, 200) with a font size of 48px bold." : "After removing 2 cookies, let’s count how many are left.",
#             "Step 8: Move 2 cookies starting from the rightmost cookie upwards from (300, 300) to (300, 100) one after the other with 0.5 seconds delay between each cookie and a fade-out effect over 0.3 seconds.": "We began with 5 cookies and removed 2.",
#             "Step 9: Apply a scale-in effect to the minus sign over 0.3 seconds." : "Now, there are 3 cookies left on the plate. ",
#             "Step 10: Add an equals sign at coordinates (450, 200) with a size of 50x50 pixels and apply a fade-in effect over 0.5 seconds." : "This shows that 5 minus 2 equals 3",
#             "Step 11: Add the number '3' at coordinates (450, 100) with a font size of 48px bold and apply a fade-in effect over 0.5 seconds." : "You now have 3 cookies left!"
#         }
#     } 

#     """
#     model = GenerativeModel(
#         model_name="gemini-1.5-pro", system_instruction=system_instruction
#     )


#     response = model.generate_content(prompt)
#     return response.text




#  **TOPIC-BASED ANIMATION GENERATION GUIDELINES**

#     **


#     Computer Science:
#     - **Artificial Intelligence (AI)**:
#     - **Neural Networks**:
#         - **Scenes**: `NeuralNetworkScene`, `ActivationScene`
#         - **Objects**: Circles (neurons), Arrows (connections), Labels (node names)
#         - **Animations/Tools**: `Create()`, `FadeIn()`, `GrowArrow()`, `ValueTracker()` for dynamic data flow.
    
#     - **Decision Trees**:
#         - **Scenes**: `DecisionTreeScene`, `PredictionScene`
#         - **Objects**: Squares (nodes), Lines (edges), Text (labels), Dots (data points)
#         - **Animations/Tools**: `DrawBorderThenFill()`, `GrowFromCenter()`, `ShowPassingFlash()` to emphasize decision points.

#     - **Machine Learning Concepts**:
#         - **Scenes**: `SupervisedLearningScene`, `UnsupervisedLearningScene`
#         - **Objects**: Data points (dots), Clusters (colored regions), Icons (tech stack)
#         - **Animations/Tools**: `ScatterPlot()`, `MoveAlongPath()`, `Create()`, `FadeOut()` for showing transitions.

#     - **Web Development**:
#     - **Frontend vs. Backend**:
#         - **Scenes**: `FrontendBackendScene`
#         - **Objects**: Two panels (for UI and server), Icons (HTML, CSS, JS), Arrows (data flow)
#         - **Animations/Tools**: `ShowIncreasingSubsets()`, `Animate()`, `FadeIn()` for UI components.

#     - **Responsive Design**:
#         - **Scenes**: `ResponsiveDesignScene`
#         - **Objects**: Webpage elements (rectangles), Breakpoints (dotted lines), Resize handles
#         - **Animations/Tools**: `Scale()`, `Shift()`, `FadeIn()` to demonstrate resizing.

#     - **Database Management**:
#     - **Normalization**:
#         - **Scenes**: `NormalizationScene`
#         - **Objects**: Tables (rectangles), Duplicates (crossed out items), Connected tables (arrows)
#         - **Animations/Tools**: `Transform()`, `DrawBorderThenFill()`, `FadeIn()` for transitions between states.

#     - **SQL Queries**:
#         - **Scenes**: `SQLQueryScene`
#         - **Objects**: SQL code display (Text), Result table (Grid), Data points (dots)
#         - **Animations/Tools**: `Write()`, `ShowPassingFlash()`, `FadeIn()` to reveal query results.

#     Algorithms:
#     - **Graph Algorithms**:
#     - **Dijkstra's Algorithm**:
#         - **Scenes**: `DijkstraScene`
#         - **Objects**: Graph nodes (circles), Edges (lines), Weights (text)
#         - **Animations/Tools**: `Create()`, `UpdateFromFunc()`, `Flash()`, `MoveAlongPath()` to visualize the path.

#     - **Minimum Spanning Tree**:
#         - **Scenes**: `MSTScene`
#         - **Objects**: Graph representation (nodes and edges), MST (highlighted edges)
#         - **Animations/Tools**: `ShowIncreasingSubsets()`, `GrowFromCenter()`, `FadeIn()` for selected edges.

#     - **Dynamic Programming**:
#     - **Fibonacci Sequence**:
#         - **Scenes**: `FibonacciScene`
#         - **Objects**: Trees (for recursion), Table (for dynamic programming)
#         - **Animations/Tools**: `Create()`, `FadeIn()`, `ValueTracker()` for visualizing recursive calls.

#     - **Knapsack Problem**:
#         - **Scenes**: `KnapsackScene`
#         - **Objects**: Items (rectangles), Capacity (bar), Decision markers (arrows)
#         - **Animations/Tools**: `ShowIncreasingSubsets()`, `Transform()`, `Flash()` for choices made.

#     Chemistry:
#     - **Organic Chemistry**:
#     - **Functional Groups**:
#         - **Scenes**: `FunctionalGroupsScene`
#         - **Objects**: Molecular structures (2D representations), Functional groups (color-coded)
#         - **Animations/Tools**: `Create()`, `FadeIn()`, `Highlight()` to demonstrate group properties.

#     - **Reactions Animation**:
#         - **Scenes**: `ReactionScene`
#         - **Objects**: Reactants and products (molecules), Bonds (lines), Reaction pathway (arrows)
#         - **Animations/Tools**: `DrawBorderThenFill()`, `Create()`, `Transform()`, `FadeIn()` to show reaction progression.

#     - **Thermodynamics**:
#     - **Laws of Thermodynamics**:
#         - **Scenes**: `ThermodynamicsScene`
#         - **Objects**: Closed system (box), Heat arrows, Work arrows
#         - **Animations/Tools**: `ShowIncreasingSubsets()`, `Create()`, `FadeIn()` to visualize energy transfer.

#     - **Phase Diagrams**:
#         - **Scenes**: `PhaseDiagramScene`
#         - **Objects**: Phase regions (color-coded), Critical points (dots)
#         - **Animations/Tools**: `Create()`, `FadeIn()`, `Highlight()` for transitions between phases.

#     Physics:
#     - **Quantum Mechanics**:
#     - **Wave-Particle Duality**:
#         - **Scenes**: `WaveParticleScene`
#         - **Objects**: Waves (sine curves), Particles (dots), Slits (rectangles)
#         - **Animations/Tools**: `Create()`, `FadeIn()`, `ShowPassingFlash()` to highlight interference patterns.

#     - **Quantum States**:
#         - **Scenes**: `QuantumStateScene`
#         - **Objects**: Vectors (arrows), Measurement apparatus (box)
#         - **Animations/Tools**: `Animate()`, `FadeIn()`, `Rotate()` to show state changes.

#     - **Electromagnetism**:
#     - **Electric Fields**:
#         - **Scenes**: `ElectricFieldScene`
#         - **Objects**: Charges (dots), Field lines (arrows), Test charge (dot)
#         - **Animations/Tools**: `Create()`, `MoveAlongPath()`, `ShowIncreasingSubsets()` for field visualization.

#     - **Magnetic Fields**:
#         - **Scenes**: `MagneticFieldScene`
#         - **Objects**: Current paths (lines), Magnetic field lines (curved arrows)
#         - **Animations/Tools**: `Create()`, `Rotate()`, `FadeIn()` to demonstrate interactions.

#     Mathematics:
#     - **Graph Theory**:
#     - **Eulerian and Hamiltonian Paths**:
#         - **Scenes**: `PathScene`
#         - **Objects**: Graph representation (nodes and edges), Paths (highlighted edges)
#         - **Animations/Tools**: `Create()`, `MoveAlongPath()`, `Flash()` to show path traversal.

#     - **Graph Coloring**:
#         - **Scenes**: `GraphColoringScene`
#         - **Objects**: Graph structure (nodes), Colors (filled shapes)
#         - **Animations/Tools**: `Create()`, `SetColor()`, `FadeIn()` to visualize coloring process.

#     - **Number Theory**:
#     - **Prime Factorization**:
#         - **Scenes**: `PrimeFactorizationScene`
#         - **Objects**: Composite numbers (rectangles), Trees (for factorization)
#         - **Animations/Tools**: `Create()`, `FadeIn()`, `Transform()` for showing factor breakdown.

#     - **Greatest Common Divisor (GCD)**:
#         - **Scenes**: `GCDScene`
#         - **Objects**: Number line, GCD markers (dots)
#         - **Animations/Tools**: `Create()`, `Flash()`, `ShowIncreasingSubsets()` for process visualization.

#     Arithmetic Operations:
#     - **Complex Numbers**:
#     - **Geometric Representation**:
#         - **Scenes**: `ComplexPlaneScene`
#         - **Objects**: Complex plane (grid), Vectors (arrows)
#         - **Animations/Tools**: `Create()`, `FadeIn()`, `Arrow()` for visualizing complex number operations.

#     - **Polar Form**:
#         - **Scenes**: `PolarFormScene`
#         - **Objects**: Polar coordinates (arrows), Conversion process (text)
#         - **Animations/Tools**: `Rotate()`, `Transform()`, `Flash()` for showing conversions.

#     - **Statistics**:
#     - **Probability Distributions**:
#         - **Scenes**: `DistributionScene`
#         - **Objects**: Graphs (curves), Data points (dots), Parameters (text)
#         - **Animations/Tools**: `Create()`, `FadeIn()`, `Animate()` for showcasing distribution changes.

#     - **Hypothesis Testing**:
#         - **Scenes**: `HypothesisTestingScene`
#         - **Objects**: Null and alternative hypothesis (text), Results (bars)
#         - **Animations/Tools**: `Create()`, `Flash()`, `ShowIncreasingSubsets()` for displaying results.

#     Biology:
#     - **Cell Biology**:
#     - **Cell Division**:
#         - **Scenes**: `CellDivisionScene`
#         - **Objects**: Cell structures (circles), Chromosomes (lines)
#         - **Animations/Tools**: `Create()`, `FadeIn()`, `ShowPassingFlash()` to highlight stages.

#     - **Photosynthesis**:
#         - **Scenes**: `PhotosynthesisScene`
#         - **Objects**: Chloroplast (circle), Light energy (arrows), Chemical reactions (text)
#         - **Animations/Tools**: `Create()`, `FadeIn()`, `ShowIncreasingSubsets()` for process visualization.

#     - **Genetics**:
#     - **Punnett Squares**:
#         - **Scenes**: `PunnettSquareScene`
#         - **Objects**: Squares (grid), Alleles (letters), Genotypes (text)
#         - **Animations/Tools**: `Create()`, `ShowPassingFlash()`, `FadeIn()` for demonstrating crosses.    
