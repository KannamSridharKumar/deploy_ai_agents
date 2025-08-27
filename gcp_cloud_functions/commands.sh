gcloud auth login
gcloud config list

gcloud config set
gcloud config set project PROJECT_ID

gcloud functions deploy ai-agent-fun \
--region=us-central1 \
--runtime=python310 \
--source=. \
--entry-point=app \
--trigger-http \
--gen2 \
--memory=256MB \
--allow-unauthenticated

gcloud artifacts repositories create my-cloud-funs-repo \
--repository-format=docker \
--location=us-central1 \
--description="Repo for Cloud Run functions"
