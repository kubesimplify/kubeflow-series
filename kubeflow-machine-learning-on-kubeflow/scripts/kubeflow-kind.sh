curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.14.0/kind-linux-amd64
chmod +x ./kind
cat > kind-config.yaml <<EOF
# two node cluster config
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
EOF
kind create cluster --name kubeflow-playground --config kind-config.yaml --image kindest/node:1.21.12
opsys=linux
wget https://github.com/kubernetes-sigs/kustomize/releases/download/v3.2.0/kustomize_3.2.0_${opsys}_amd64
mv https://github.com/kubernetes-sigs/kustomize/releases/download/v3.2.0/kustomize_3.2.0_${opsys}_amd64 kustomize
chmod u+x kustomize

git clone https://github.com/kubeflow/manifests
cd manifests
while ! ../kustomize build example | kubectl apply -f -; do echo "Retrying to apply resources"; sleep 10; done