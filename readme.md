# Docker and EKS Deployment Guide

## Docker and Docker-Compose Deployment in a Local Environment

To deploy your application and database in containers locally, follow these steps:

### 1. Install Docker and Docker Compose
- First, install Docker:
    ```bash
    sudo apt install docker
    ```
- Verify the installation:
    ```bash
    docker --version
    ```

### 2. Create a Dockerfile
- Create a `Dockerfile` for your application.
- Test the Dockerfile by building the image and running the container:
    ```bash
    docker build -t app_image .
    docker run -it --name app -p 97:50000 app_image
    ```

### 3. Access the Application
- Check if your application is running by accessing it at `http://127.0.0.1:97`.

### 4. Create a Docker Compose File
- Create a `docker-compose.yml` file to deploy both the application and the database.
- Run the following commands:
    ```bash
    docker-compose build
    docker-compose up
    ```

---

## EKS Deployment Steps

### 1. Set Up an EKS Cluster in the AWS Console
- Go to the EKS section in the AWS Console.
- Create a new EKS cluster and give it a name.
- Create an IAM role for the cluster and set the necessary permissions.
- Create an IAM role for the node and set the necessary permissions.
- Select the default VPC and subnets.

### 2. Create an IAM User for AWS CLI Access
- Create a new IAM user and generate an access key and secret access key.

### 3. Configure AWS CLI
- On your local system, configure the AWS CLI:
    ```bash
    aws configure
    ```

### 4. Set Up the EKS Node Group
- In the EKS console, go to the **Compute** tab and configure the node group:
    - **Step 1**: Configure the node group.
    - **Step 2**: Set up compute and scaling configurations.
    - **Step 3**: Specify networking settings.
    - **Step 4**: Review and create the node group.

### 5. Configure `kubectl` for EKS
- On your local system, update the Kubernetes configuration for the EKS cluster:
    ```bash
    aws eks --region ap-south-1 update-kubeconfig --name mycluster
    ```

### 6. Deploy Using Kubernetes
- Deploy your application using `kubectl`:
    ```bash
    kubectl apply -f deployment.yml
    kubectl apply -f service.yml
    ```

---

Your application should now be deployed both locally using Docker and Docker Compose and on AWS EKS for a scalable solution.
