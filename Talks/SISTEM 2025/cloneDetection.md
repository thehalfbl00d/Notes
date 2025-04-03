# Clone 

### Clone Drift

##### Heavy emphasis on ML

#### - Type 1
- Exact copy with no modifications.
#### - Type 2
- Copy with minor modifications, such as renaming variables or changing comments.
#### - Type 3
- Copy with more significant changes, including added or removed lines of code.
#### - Type 4
- Conceptual similarity without direct copying of code.

### Precision vs Accuracy

- **Precision**: Refers to how close the results of repeated measurements or detections are to each other. It measures consistency.
- **Accuracy**: Refers to how close a measurement or detection is to the true or actual value. It measures correctness.

## History
- Type 1/2 are very easily comparable.
- Neural networks (NN) are effective at Type 3/4 comparison.

### Solution (Phase 1)
- A BERT-based approach:
  - **BERT (Bidirectional Encoder Representations from Transformers)** is a transformer-based model designed for natural language understanding.
  - It can be fine-tuned for code similarity detection by training on labeled datasets of code clones.
  - The model captures semantic meaning, making it effective for detecting Type 3 and Type 4 clones.
- **Expected Result**: SSCD (Semantic Similarity for Clone Detection).
- **Steps**:
  1. Preprocess the code to tokenize and normalize it.
  2. Fine-tune a pre-trained BERT model on a dataset of labeled code pairs.
  3. Use the fine-tuned model to compute similarity scores between code snippets.
  4. Classify pairs based on a similarity threshold.

### SSCD (Semantic Similarity for Clone Detection)

- SSCD is a method to identify code clones by analyzing the semantic meaning of code rather than just its syntax.
- It focuses on understanding the functionality and intent of the code to detect deeper similarities.

### CodeBERT and GraphBERT in SSCD

- **CodeBERT**:
  - A pre-trained model specifically designed for programming languages.
  - It is trained on a large corpus of code and natural language pairs, making it effective for understanding code semantics.
  - In SSCD, CodeBERT can be used to capture the textual and structural features of code, making it suitable for detecting Type 3 and Type 4 clones.

- **GraphBERT**:
  - A model designed to work with graph-structured data.
  - It can represent code as graphs (e.g., Abstract Syntax Trees or Control Flow Graphs) and learn relationships between nodes.
  - In SSCD, GraphBERT can complement CodeBERT by focusing on the structural and relational aspects of code, improving detection of complex clones.

- **Integration into SSCD**:
  - CodeBERT and GraphBERT can be combined to leverage both semantic and structural information.
  - CodeBERT handles textual and semantic similarity, while GraphBERT focuses on structural relationships.
  - Together, they provide a comprehensive approach to clone detection, especially for Type 3 and Type 4 clones.

### SSCD (T5+)

- **T5 (Text-to-Text Transfer Transformer)**:
  - A transformer model that treats all tasks as text-to-text problems, making it highly flexible.
  - T5+ refers to an enhanced or fine-tuned version of T5 for specific tasks, such as code understanding and similarity detection.
- **Role in SSCD**:
  - T5+ can be fine-tuned on code datasets to generate embeddings or textual representations of code.
  - It excels at capturing both semantic and contextual information, making it effective for detecting Type 3 and Type 4 clones.
- **Advantages**:
  - Handles multi-modal inputs (e.g., code and comments) effectively.
  - Can be used for tasks like code summarization, translation, and similarity detection.
- **Integration**:
  - T5+ can complement CodeBERT and GraphBERT by providing a unified text-to-text framework.
  - It can be used to preprocess or postprocess code representations, enhancing the overall SSCD pipeline.