# Deploying a Streamlit application in AWS: An end-to-end tutorial

It's a simple application that is currently using Stream as the front-end. I will show you can take this existing Streamlit app and deploy it on AWS 

## Get started

> Before you deploy your Streamlit app, make sure it works locally

- Launch a Amazon EC2 instance using free tier

- Install all the required libraries/packages

- Run the Streamlit app

- Open the app on the browser

- Point your NAMECHEAP domain name to your AWS EC2 Linux instance

1. Launch an Amazon EC2 instance

- Before we start with using the amazon ec2 instance, we need to set one up. You might need to sign up with your email ID and set up the payment information on the AWS website. Works just like a simple sign-on. From here, I will assume that you have an AWS account and so I am going to explain the next essential parts so you can follow through.

- Go to AWS Management Console using https://us-west-2.console.aws.amazon.com/console.

- On the AWS Management Console, you can select “Launch a Virtual Machine”. Here we are trying to set up the machine where we will deploy our Streamlit app.

- In the first step, you need to choose the AMI template for the machine. I select the 18.04 Ubuntu Server since it is applicable for the Free Tier. And Ubuntu.

- In the second step, I select the t2.micro instance as again it is the one which is eligible for the free tier. As you can see t2.micro is just a single CPU instance with 512 MB RAM. You can opt for a bigger machine if you are dealing with a powerful model or are willing to pay.

- Keep pressing Next until you reach the “6. Configure Security Group” tab. You will need to add a rule with Type: “Custom TCP Rule”, Port Range:8501, and Source: MyIP. We use the port 8501 here since it is the custom port used by Streamlit.

- You can click on “Review and Launch” and finally on the “Launch” button to launch the instance. Once you click on Launch you might need to create a new key pair

- You can now go to your instances to see if your instance has started. Hint: See the Instance state, it should be showing “Running”

- Select your instance, and copy the Public DNS(IPv4) Address from the description. It should be something starting with ec2.

2. Install all the packages/dependencies

After all the above steps you should be able to see the ubuntu prompt for the virtual machine. We will need to set up this machine to run our app. I am going to be using this app for the demonstration purposes

```
$ git clone https://github.com/upendrak/streamlit-aws-tutorial.git
$ cd streamlit-aws-tutorial
```

```
$ sudo apt update
$ sudo apt get install -y python3-pip
$ pip3 install -r requirements.txt
$ export PATH=~/.local/bin/:$PATH
```

Once the dependencies are installed without any errors, your machine is now prepped and ready to run.

- Running Streamlit on Amazon ec2

```
streamlit run app.py
```
After running the streamlit, you'll find the following ip address

```
You can now view your Streamlit app in your browser.

  Network URL: http://172.31.41.84:8501
  External URL: http://18.224.200.50:8501
```

3. Open the app on the browser

Now you can go to a browser and type the external URL to access your app. In my case the address is http://18.224.200.50:8501. Here is the output. This app will be up right now if you want to play with it.


4. Run Streamlit in the background

You can use 'screen' or 'tmux' to run streamlit in the background


5. Associate domain to Amazon EC2 instance (Optional)

If you want to associate a domain to your Amazon EC2 instance (so that you don't carry around with this <ip_address>:<8501>), then you can use [Namecheap](https://www.namecheap.com/). Here are the brief [instructions](https://u.osu.edu/walujo.1/2016/07/07/associate-namecheap-domain-to-amazon-ec2-instance/) 
