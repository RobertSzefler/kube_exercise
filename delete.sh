ORG_CURDIR=$(pwd)
MY_DIR=$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")

echo "$(tput bold)Kubernetes: destroying...$(tput sgr 0)"
cd "$MY_DIR"
kubectl delete -f mongo-config.yaml
kubectl delete -f mongo-secret.yaml
kubectl delete -f mongo-deployment.yaml
kubectl delete -f api-deployment.yaml
kubectl delete -f main-deployment.yaml

cd $ORG_CURDIR
