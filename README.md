# Azure ML Inference Pipeline 🚀

This project is a complete AI/ML pipeline deployed on Microsoft Azure, designed for real-time inference, model training, infrastructure-as-code, and document-based Retrieval-Augmented Generation (RAG) using LangChain and FAISS.

---

## 📁 Project Structure

```
azure-ml-inference-pipeline/
│
├── infrastructure/           # Terraform code for Azure infra (AKS, ACR, Azure ML, Key Vault)
├── ml_models/                # Model training scripts using sklearn + MLflow logging
├── app/                      # FastAPI inference service with Docker support
├── cognitive_search_rag/     # LangChain-based RAG pipeline + document ingestion
├── .github/workflows/        # GitHub Actions CI/CD for model training + infra deployment
└── README.md                 # You are here!
```

---

## ⚙️ Tech Stack

- **Azure AKS, ACR, Azure ML, Key Vault**
- **Terraform** for IaC
- **FastAPI + Docker** for inference
- **LangChain + FAISS** for RAG
- **GitHub Actions** for CI/CD
- **MLflow** for experiment tracking
- **Python + scikit-learn** for model training

---

## 🔧 Setup Instructions

### 1. Provision Azure Infrastructure
```bash
cd infrastructure
terraform init
terraform apply -auto-approve
```

> Make sure to replace `tenant_id` in `main.tf` with your Azure AD tenant ID.

### 2. Train Model
```bash
cd ml_models/diabetes_model
python train.py
python mlflow_tracking.py  # optional
```

### 3. Run FastAPI Inference Locally
```bash
cd app
uvicorn main:app --reload
```

Or use Docker:
```bash
docker build -t fastapi-infer .
docker run -p 8000:8000 fastapi-infer
```

### 4. Create FAISS Vector Store for RAG
```bash
cd cognitive_search_rag
python document_loader.py
python rag_pipeline.py
```

> Add `.txt` files to the `docs/` folder before running.

---

## ✅ GitHub Actions

- **CI** (`ci.yml`) – Lint, test, and train model
- **CD** (`cd.yml`) – Terraform plan/apply for Azure deployment

---

## 📞 Support

For questions, reach out to [Siva](mailto:sra98487@gmail.com)  
LinkedIn: [https://www.linkedin.com/in/siva-a-96b738224](https://www.linkedin.com/in/siva-a-96b738224)

---

## 📄 License
MIT
