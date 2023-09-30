ORG_CURDIR=$(pwd)
MY_DIR=$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")

export DOCKER_CLI_HINTS=false

echo "$(tput bold)Build: main app...$(tput sgr 0)"
cd $MY_DIR/main && ./build.sh
echo "$(tput bold)Build: API app...$(tput sgr 0)"
cd $MY_DIR/api && ./build.sh
echo "$(tput bold)Clean up Docker images...$(tput sgr 0)"
docker image prune -f
echo "$(tput bold)Docker images info$(tput sgr 0)"
docker images
echo "$(tput bold)Kubernetes deploy...$(tput sgr 0)"
cd "$MY_DIR"
# minikube image load robertszefler/flask-kub-main
# minikube image load robertszefler/flask-kub-api
kubectl apply -f mongo-config.yaml
kubectl apply -f mongo-secret.yaml
kubectl apply -f mongo-deployment.yaml
# XXX this is hackish
VERSION=$(cat api/VERSION) envsubst < api-deployment.yaml | kubectl apply -f -
VERSION=$(cat main/VERSION) envsubst < main-deployment.yaml | kubectl apply -f -
echo "$(tput bold)Kubernetes cluster info$(tput sgr 0)"
kubectl get all

cd $ORG_CURDIR
