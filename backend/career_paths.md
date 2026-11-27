# Career Paths in Data Science, AI and ML: Career Coach Knowledge Base

## At a glance

This document describes four career paths in Data Science, AI and ML: **Data Scientist**, **Machine Learning Engineer**, **AI Engineer** and **MLOps Engineer**. Each path section has the same parts (role, prerequisites, mandatory skills, good-to-have skills, career progression, first steps and keywords), so a career coach agent can search it and answer questions like "What do I need to become an ML engineer?" or "I know Python and SQL, which path suits me?"

| Path | Core question it answers | Closest starting background | Strongest skill area | Main output |
|---|---|---|---|---|
| Data Scientist | What does the data tell us, and what should we do? | Statistics, maths, analytics, economics | Statistics and experimentation | Insights, models, experiment results |
| Machine Learning Engineer | How do we build a model that works reliably in a product? | Software engineering, computer science | ML algorithms plus software engineering | Trained models and ML services |
| AI Engineer | How do we build useful products on top of large language models? | Software or full-stack development | LLM application development | Chatbots, agents, RAG systems, AI features |
| MLOps Engineer | How do we deploy, monitor and scale models safely? | DevOps, cloud, backend engineering | Infrastructure and automation | ML pipelines, platforms, monitoring |

**Notes for the agent:** match the user's question to the **Keywords** line at the end of each path first. Treat skill lists as typical industry expectations, not fixed rules; job descriptions vary by company and country. Experience ranges in the progression tables are approximate.

## Path 1: Data Scientist

**Role.** A data scientist turns data into decisions. They clean and explore data, run experiments such as A/B tests, build predictive models, and explain results to business teams. The job sits between analysis and engineering, with a strong emphasis on statistics and communication.

**Typical work:** defining metrics, analysing customer behaviour, forecasting demand, building churn or fraud models, designing experiments, and presenting findings to managers.

**Prerequisites**

- A degree in a quantitative field (statistics, mathematics, computer science, economics, engineering, physics) is common, though not strictly required if skills are proven through projects.
- Comfort with school and college-level maths: algebra, basic calculus and probability.
- Basic programming experience in any language.

**Mandatory skills**

| Skill area | What to know |
|---|---|
| Python | pandas, NumPy, Matplotlib or Seaborn, Jupyter notebooks |
| SQL | Joins, aggregations, window functions, subqueries |
| Statistics | Distributions, hypothesis testing, confidence intervals, p-values, regression |
| Machine learning basics | Linear and logistic regression, decision trees, random forests, gradient boosting, clustering, using scikit-learn |
| Model evaluation | Train-test split, cross-validation, accuracy, precision, recall, F1, ROC-AUC, RMSE, overfitting |
| Data wrangling | Handling missing values, outliers, feature engineering, encoding categories |
| Communication | Explaining results to non-technical people, building clear charts and dashboards |

**Good-to-have skills:** experimentation and causal inference, time-series forecasting, a BI tool (Power BI or Tableau), Spark for large data, basic deep learning, domain knowledge (finance, healthcare, retail).

**Career progression**

| Level | Typical experience | Focus |
|---|---|---|
| Data Analyst (common entry point) | 0 to 2 years | SQL, reports, dashboards, descriptive analysis |
| Junior Data Scientist | 0 to 2 years | Analysis and simple models under guidance |
| Data Scientist | 2 to 5 years | Owns projects end to end, from question to model to recommendation |
| Senior Data Scientist | 5 to 8 years | Leads complex problems, mentors others, shapes metrics |
| Lead or Principal Data Scientist, or Data Science Manager | 8+ years | Sets direction across teams; technical or people leadership |

**First steps**

1. Learn Python and SQL until you can answer questions from a real dataset without help.
2. Study statistics properly, especially hypothesis testing and regression.
3. Build three portfolio projects with a clear business question, such as churn prediction, sales forecasting and an A/B test analysis. Publish them on GitHub with a short write-up.
4. Practise explaining each project in five minutes to a non-technical listener.

**Keywords:** data science, data scientist, data analyst, statistics, analytics, A/B testing, experiments, insights, dashboards, pandas, SQL, scikit-learn, predictive modelling, forecasting, business decisions.

## Path 2: Machine Learning Engineer

**Role.** A machine learning engineer builds models that run reliably inside real products. Where a data scientist asks "does this model work?", an ML engineer asks "does it work at scale, every day, for millions of users?" The role combines ML knowledge with solid software engineering.

**Typical work:** training and tuning models, building feature pipelines, serving models through APIs, optimising speed and cost, and working on systems such as recommendations, search ranking, computer vision or speech.

**Prerequisites**

- A degree in computer science, engineering or a related field is common. Strong software engineers from any background can move in.
- Good programming ability: data structures, algorithms, writing clean and tested code.
- Maths for ML: linear algebra (vectors, matrices), calculus (gradients), probability.

**Mandatory skills**

| Skill area | What to know |
|---|---|
| Python and software engineering | Clean code, testing, Git, object-oriented design, debugging |
| ML algorithms | Supervised and unsupervised learning, bias-variance trade-off, regularisation, gradient boosting |
| Deep learning | Neural networks, backpropagation, CNNs, transformers, with PyTorch or TensorFlow |
| Data processing | pandas, SQL, building reproducible feature pipelines |
| Model evaluation | Choosing metrics, validation strategy, error analysis, avoiding data leakage |
| Model serving | Exposing a model through a REST API (for example FastAPI), batch versus real-time inference |
| Tooling | Linux command line, Docker, one cloud platform (AWS, GCP or Azure) |

**Good-to-have skills:** distributed training, GPU optimisation, model compression and quantisation, recommender systems, computer vision or NLP specialisation, Spark, experiment tracking (MLflow or Weights & Biases).

**Career progression**

| Level | Typical experience | Focus |
|---|---|---|
| Junior ML Engineer | 0 to 2 years | Implementing and testing models and pipelines under guidance |
| ML Engineer | 2 to 5 years | Owns models in production, from training to serving |
| Senior ML Engineer | 5 to 8 years | Designs ML systems, sets standards, mentors |
| Staff or Principal ML Engineer | 8+ years | Architecture across teams, long-term technical direction |
| ML Engineering Manager | 8+ years | Leads teams of ML engineers (people track) |

**First steps**

1. If you come from data science, strengthen software engineering: testing, Git, APIs and Docker.
2. If you come from software, learn the ML fundamentals first, then deep learning with PyTorch.
3. Build one project end to end: train a model, wrap it in a FastAPI service, containerise it with Docker and deploy it to the cloud.
4. Read and reimplement one well-known paper or model architecture.

**Keywords:** machine learning engineer, ML engineer, model training, deep learning, PyTorch, TensorFlow, neural networks, model deployment, model serving, recommendation systems, computer vision, NLP, production ML, software engineering.

## Path 3: AI Engineer (Generative AI and LLM applications)

**Role.** An AI engineer builds products on top of large language models (LLMs) and other foundation models, usually through APIs rather than training models from scratch. This is the newest of the four paths and grew quickly with tools like chat assistants, coding agents and AI search.

**Typical work:** building chatbots and AI assistants, retrieval-augmented generation (RAG) over company documents, agents that call tools, prompt design, evaluating answer quality, and adding AI features to existing apps.

**Prerequisites**

- Solid programming in Python or JavaScript/TypeScript. Many AI engineers start as backend or full-stack developers.
- Understanding of web basics: REST APIs, JSON, HTTP, databases.
- A degree helps but is less important here than a strong portfolio of working AI apps.

**Mandatory skills**

| Skill area | What to know |
|---|---|
| Programming | Python (or TypeScript), async code, calling REST APIs, error handling |
| LLM fundamentals | Tokens, context windows, temperature, how transformers work at a high level, model strengths and limits |
| Prompt engineering | System prompts, few-shot examples, structured output (JSON), reducing hallucinations |
| RAG | Chunking documents, embeddings, vector databases, retrieval and re-ranking, citing sources |
| Agents and tools | Tool calling, agent loops, frameworks such as LangChain and LangGraph, memory (checkpointers and stores) |
| Evaluation | Building test sets, measuring answer quality, LLM-as-judge, tracing with tools like LangSmith |
| App development | Backend APIs (FastAPI or Node.js), a frontend (React), deployment basics |

**Good-to-have skills:** fine-tuning, multimodal models (images, audio), guardrails and safety, cost and latency optimisation, the Model Context Protocol (MCP), classic ML basics for context.

**Career progression**

| Level | Typical experience | Focus |
|---|---|---|
| Junior AI Engineer | 0 to 2 years | Building features with LLM APIs, prompts and simple RAG |
| AI Engineer | 2 to 5 years | Owns AI features end to end, including evaluation |
| Senior AI Engineer | 5 to 8 years | Designs agent and RAG architectures, reliability, cost control |
| Staff AI Engineer or AI Architect | 8+ years | Sets AI platform and product direction across teams |
| Head of AI or AI Engineering Manager | 8+ years | Leads AI product teams (people track) |

Experience in this path often counts software engineering years, since the LLM field itself is young.

**First steps**

1. Build a simple chatbot with an LLM API and a system prompt.
2. Add RAG: load a few documents, embed them, and answer questions with citations.
3. Build an agent with LangGraph that uses tools and remembers users, like the CareerBuddy assignment.
4. Write an evaluation set of 20 questions and measure how often your app answers correctly.

**Keywords:** AI engineer, generative AI, GenAI, LLM, large language models, prompt engineering, RAG, retrieval, embeddings, vector database, agents, LangChain, LangGraph, chatbot, AI assistant, Claude, tool calling.

## Path 4: MLOps Engineer

**Role.** An MLOps engineer builds the platform that lets models move from a notebook to production and stay healthy there. They automate training and deployment, monitor models for drift and failures, and make ML work repeatable. It is DevOps applied to machine learning.

**Typical work:** building CI/CD pipelines for models, setting up model registries and experiment tracking, deploying models on Kubernetes or cloud ML services, monitoring accuracy and data drift, and managing compute cost.

**Prerequisites**

- A background in DevOps, cloud, backend or platform engineering is the most common route in.
- Strong Linux and scripting skills.
- Enough ML understanding to know how models are trained, evaluated and why they degrade over time.

**Mandatory skills**

| Skill area | What to know |
|---|---|
| Programming | Python and Bash scripting; writing reliable automation |
| Containers | Docker images, Kubernetes deployments, scaling services |
| CI/CD | GitHub Actions, GitLab CI or Jenkins; automated testing and releases |
| Cloud | One platform in depth (AWS, GCP or Azure), including its ML service (SageMaker, Vertex AI or Azure ML) |
| ML lifecycle tools | Experiment tracking and model registry (MLflow), pipeline orchestration (Airflow, Kubeflow or Prefect) |
| Monitoring | Logging, metrics and alerts (Prometheus, Grafana); model and data drift detection |
| ML basics | Training, validation, metrics, retraining triggers, data versioning |

**Good-to-have skills:** infrastructure as code (Terraform), feature stores, GPU cluster management, serving frameworks for LLMs, security and access control, cost optimisation.

**Career progression**

| Level | Typical experience | Focus |
|---|---|---|
| Junior MLOps or DevOps Engineer | 0 to 2 years | Maintaining pipelines and deployments under guidance |
| MLOps Engineer | 2 to 5 years | Owns deployment and monitoring for ML systems |
| Senior MLOps Engineer | 5 to 8 years | Designs the ML platform, sets reliability standards |
| ML Platform Lead or Staff Engineer | 8+ years | Platform strategy across teams |
| Head of ML Platform or Infrastructure Manager | 8+ years | Leads platform teams (people track) |

**First steps**

1. Learn Docker and Linux well, then basic Kubernetes.
2. Take a simple trained model and build a pipeline that retrains, tests and redeploys it automatically when code changes.
3. Add MLflow for experiment tracking and a model registry.
4. Add monitoring: log predictions and alert when the input data drifts from the training data.

**Keywords:** MLOps, ML platform, DevOps, model deployment, CI/CD, Docker, Kubernetes, MLflow, Airflow, Kubeflow, monitoring, model drift, cloud, AWS, GCP, Azure, SageMaker, Vertex AI, infrastructure.

## Choosing a path

The best path depends on what the user already knows and what kind of work they enjoy. The agent should ask about both before recommending.

**Matching by background**

| User's background | Most natural first path | Also worth considering |
|---|---|---|
| Fresh graduate, maths or statistics | Data Scientist (often via Data Analyst) | ML Engineer |
| Fresh graduate, computer science | ML Engineer or AI Engineer | Data Scientist |
| Data or business analyst | Data Scientist | AI Engineer |
| Backend or full-stack developer | AI Engineer | ML Engineer |
| DevOps, cloud or system administrator | MLOps Engineer | ML Engineer |
| Domain expert (finance, healthcare, marketing) | Data Scientist | AI Engineer for domain AI tools |

**Matching by interest**

- Enjoys finding patterns and explaining "why" to people: **Data Scientist**.
- Enjoys building systems, writing code and solving performance problems with models: **ML Engineer**.
- Enjoys building apps and products quickly, and is excited by LLMs and agents: **AI Engineer**.
- Enjoys automation, infrastructure and keeping systems reliable: **MLOps Engineer**.

**Skills shared by all four paths:** Python, Git, basic SQL, understanding of how ML models are trained and evaluated, and the ability to explain technical work clearly. A user who is unsure can start with these while deciding.

**Switching between paths**

- Data Scientist to ML Engineer: add software engineering, APIs, Docker and deployment.
- ML Engineer to AI Engineer: add prompt engineering, RAG, agents and LLM evaluation.
- Software Developer to AI Engineer: add LLM fundamentals, RAG and agents; this is one of the shortest switches.
- DevOps Engineer to MLOps Engineer: add ML basics and ML lifecycle tools like MLflow.

**How the coach should respond:** recommend one primary path with reasons tied to the user's background, list the mandatory skills they already have and the ones they still need, and suggest the next two or three concrete steps from that path's **First steps**.
