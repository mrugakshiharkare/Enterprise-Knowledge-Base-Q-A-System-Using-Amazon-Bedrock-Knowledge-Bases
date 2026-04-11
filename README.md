# Enterprise Knowledge Base Q&A System 🚀

An end-to-end Generative AI application that implements **Retrieval-Augmented Generation (RAG)** using **Amazon Bedrock**. This system allows users to upload enterprise documents to an S3 bucket and query them through a web-based chat interface.

## 🏗️ Architecture
The application follows a modern cloud-native RAG workflow:
1. **Data Source:** PDF/Text documents stored in **Amazon S3**.
2. **Orchestration:** **Amazon Bedrock Knowledge Bases** manages the vectorization and retrieval.
3. **Foundation Model:** **Amazon Nova 2 Lite** (via Cross-Region Inference Profiles) for high-performance, low-latency text generation.
4. **Frontend:** **Streamlit** UI hosted on **AWS EC2**.



## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Cloud:** AWS (Bedrock, S3, EC2, IAM)
* **SDK:** Boto3 (AWS SDK for Python)
* **Web Framework:** Streamlit
* **LLM:** Amazon Nova 2 Lite

## 🚀 Key Features
* **Contextual Accuracy:** Uses RAG to ensure answers are grounded in provided documents, reducing hallucinations.
* **Cloud-Native Scalability:** Built entirely on AWS serverless infrastructure for model inference.
* **Real-time Interaction:** Streamlined chat interface for enterprise users to query complex documentation.

## 📋 Prerequisites
* AWS Account with Bedrock model access enabled (Nova 2 Lite).
* Configured Bedrock Knowledge Base and Data Source.
* EC2 Instance (Ubuntu) with Python installed.

## ⚙️ Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/mrugakshiharkare/Enterprise-Knowledge-Base-Q-A-System-Using-Amazon-Bedrock-Knowledge-Bases.git](https://github.com/mrugakshiharkare/Enterprise-Knowledge-Base-Q-A-System-Using-Amazon-Bedrock-Knowledge-Bases.git)
   cd Enterprise-Knowledge-Base-Q-A-System-Using-Amazon-Bedrock-Knowledge-Bases
2. **Set up Virtual Environment:**
   ```bash
    python3 -m venv venv
    source venv/bin/activate
3. **Install Dependencies:**  
pip install -r requirements.txt
4. **Run the Application:**  
streamlit run app.py

## 🛡️ Future Enhancements
* **Guardrails for Amazon Bedrock:** Implement content filtering and PII masking to ensure safer, more compliant AI responses.
* **Multi-modal Processing:** Expand the RAG pipeline to process and retrieve information from complex tables and images within documents.
* **Persistent Vector Storage:** Migrate from managed knowledge base memory to a dedicated **Amazon OpenSearch** index for advanced metadata filtering and faster retrieval at scale.
* **Memory Integration:** Add session-state handling to allow the assistant to remember previous parts of the conversation.

