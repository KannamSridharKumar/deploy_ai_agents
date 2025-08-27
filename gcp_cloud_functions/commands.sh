gcloud auth login
gcloud config list

gcloud config set
gcloud config set project PROJECT_ID

gcloud functions deploy my-ml-app \
    --region=us-central1 \
    --runtime=python310 \
    --source=. \
    --entry-point=app \
    --trigger-http \
    --memory=256MB \
    --allow-unauthenticated




gcloud functions deploy my-ml-test \
  --gen2 \
  --region=us-central1 \
  --runtime=python310 \
  --source=. \
  --entry-point=app \
  --trigger-http \
  --memory=256MB \
  --allow-unauthenticated 


  gcloud functions deploy ai-agent-fun \
    --region=us-central1 \
    --runtime=python310 \
    --source=. \
    --entry-point=app \
    --trigger-http \
    --gen2 \
    --memory=256MB \
    --allow-unauthenticated



  gcloud functions deploy my-ml-app \
    --gen2 \
    --region=us-central1 \
    --runtime=python310 \
    --source=. \
    --entry-point=app \
    --trigger-http \
    --memory=256MB \
    --allow-unauthenticated \
    --docker-repository=us-central1-docker.pkg.dev/$(gcloud config get-value project)/my-functions-repo/my-ml-app

  
  

  gcloud artifacts repositories create my-functions-repo \
    --repository-format=docker \
    --location=us-central1 \
    --description="Repo for Cloud Run functions"


    curl -X POST https://my-ml-test-hqo2ttu27q-uc.a.run.app \
     -H "Content-Type: application/json" \
     -d '{"message":"Hello"}'


  curl -X POST https://us-central1-sri-nana.cloudfunctions.net/my-ml-test \
     -H "Content-Type: application/json" \
     -d '{"name":"Hello"}'