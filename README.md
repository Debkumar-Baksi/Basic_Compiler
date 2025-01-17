### README: Basic Compiler in Python

---

## **Basic Compiler: Turning Math Expressions into Machine Code**

### **Introduction**
This project showcases a **basic compiler** developed using Python. It takes basic mathematical expressions as input and translates them into machine code through a structured pipeline. This demonstrates my expertise in **compiler design principles** and highlights my ability to implement critical components of a compiler, such as lexical analysis, parsing, semantic analysis, intermediate code generation, and assembly code generation.

### **Features**
1. **Lexer (Lexical Analyzer):**  
   - Scans the input expression and tokenizes it into meaningful units like numbers, operators, and symbols.

2. **Parser:**  
   - Analyzes the tokens to check the syntactic structure of the expression, ensuring it follows mathematical rules.

3. **Semantic Analyzer:**  
   - Validates the semantic meaning of the expression (e.g., ensuring valid operations and operands).

4. **Three-Address Code (TAC) Generator:**  
   - Converts the expression into an intermediate representation for easier optimization and further translation.

5. **Assembly Code Generator:**  
   - Generates simplified machine-level assembly instructions from the TAC.

### **How It Works**
1. Input a mathematical expression (e.g., `3 + 5 * (2 - 8)`).
2. The compiler processes the expression through each stage:
   - Tokenization by the lexer.
   - Syntax tree construction by the parser.
   - Semantic checks.
   - TAC generation (e.g., `t1 = 2 - 8`, `t2 = 5 * t1`, `t3 = 3 + t2`).
   - Assembly code output (e.g., simplified machine code for the target architecture).

3. Outputs the machine code, demonstrating the entire transformation pipeline.

### **Demonstrating My Strengths**
This project illustrates my deep understanding of:
- **Compiler Design Concepts:**  
   Implementing the complete pipeline from lexical analysis to code generation.
- **Problem-Solving Skills:**  
   Breaking down complex tasks into modular components.
- **Python Programming Expertise:**  
   Using Python for effective implementation of compiler components.
- **Mathematical Reasoning:**  
   Translating mathematical expressions into low-level machine representations.

### **How to Run the Project**
1. Clone this repository:  
   ```bash
   git clone <repository-link>
   ```
2. Navigate to the project directory:  
   ```bash
   cd basic-compiler
   ```
3. Run the main script:  
   ```bash
   python compiler.py
   ```
4. Input a mathematical expression and see the generated machine code.

### **Future Enhancements**
- Add support for more complex expressions and data types.
- Introduce optimization techniques in the TAC stage.
- Expand assembly code generation to support additional architectures.

### **Conclusion**
This basic compiler is a testament to my ability to design and implement a functional compiler. It demonstrates my knowledge and skills in the field of **compiler design**, making it a cornerstone project in my journey as a computer scientist. 

Feel free to explore, contribute, or provide feedback!
