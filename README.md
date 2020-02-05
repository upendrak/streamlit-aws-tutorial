# Deploying a Streamlit application in AWS: An end-to-end tutorial

It's a simple application that is currently using Stream as the front-end. I will show you can take this existing Streamlit app and deploy it on AWS 

## Get started

> Before you deploy your Streamlit app, make sure it works locally

1. Launch a Amazon EC2 instance using free tier

2. Clone this github repo ont Ec2 instance

3. Install all the requirements

4. Run the Streamlit app in the background

5. Open the app on the browser

6. Point your NAMECHEAP domain name to your AWS EC2 Linux instance

7. There is no step 7

1. Launch an Amazon EC2 instance

- Before we start with using the amazon ec2 instance, we need to set one up. You might need to sign up with your email ID and set up the payment information on the AWS website. Works just like a simple sign-on. From here, I will assume that you have an AWS account and so I am going to explain the next essential parts so you can follow through.

- Go to AWS Management Console using https://us-west-2.console.aws.amazon.com/console.

- On the AWS Management Console, you can select “Launch a Virtual Machine”. Here we are trying to set up the machine where we will deploy our Streamlit app.

- In the first step, you need to choose the AMI template for the machine. I select the 18.04 Ubuntu Server since it is applicable for the Free Tier. And Ubuntu.

- 