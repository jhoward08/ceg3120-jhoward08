# Project_03 README
Objectives:
* Understand what a private cloud network is and how to build one.
* Understand what an EC2 instance is and how to make one.
--------------------------------
# Build a Virtual Private Cloud (VPC)
1. Log into the Amazon Web Service (AWS) account.
* Log into the AWS account assigned to the user using a web browser.
## insert aws_login.jpeg
--------------------------------
2. Find VPC in AWS.
* At the top left side of the screen will be a "services" dropdown button. Click on this and 
navigate down to the "Networking & Content Delivery" section which holds the VPC hyperlink.
## insert aws_services.jpeg
* This will take you to another screen with more hyperlinks and we need to click on the first 
"Resource by Region" VPCs hyperlink.
## insert aws_vpcs.jpeg
## insert aws_vpcs2.jpeg
--------------------------------
3. Create a NEW VPC.
* At the top right side of the AWS VPC page, click on the orange "Create VPC" button.
This will take you to the "Create VPC" page.
## insert aws_createVPC.jpeg
* In the "Name tag..." text box input the user's last name with "-VPC" appended to the end.
* Specify a "IPv4 CIDR block" with a private ip address range with a CIDR of /24.
## insert aws_createVPC2.jpeg
* Leave "Tenancy" as Default and "Tags" should be autopopulated for you. Click the "Create VPC"
button at the bottom of the page.
## insert aws_createVPC3.jpeg
## insert aws_createVPC4.jpeg
--------------------------------
4. Create a Subnet
* In the left banner there is a list of VPC settings, click on "Subnets".
This will take you to another screen similar to the VPC creation.
## insert aws_createSubnet.jpeg
* Click on the "Create Subnet" button and fill in the next page's text boxes similar to the VPC.
## insert aws_createSubnet2.jpeg
* Click on the dropdown and select the user made VPC.
## insert aws_createSubnet3.jpeg
* In the "Subnet name" textbox, put the user's last name and append "-Subnet" to the end of it.
* The "Availability Zone" can be left as NO PREFERENCE or pick one. I picked the first one.
* Input an "IPv4..." with a CIDR of /28, and click the "Create Subnet" button.
## insert aws_createSubnet4.jpeg
## insert aws_createSubnet5.jpeg
--------------------------------
4. Create a Gateway
* In the left banner there is a list of VPC settings, click on "Gateway".
This will take you to another screen similar to the VPC and Subnet creation.
## insert aws_createSubnet.jpeg
* Click on the "Create internet gateway" button and fill in the next page's "Name tag" with the
user's last name and append "-GW" to the end.
## insert aws_createGW.jpeg
## insert aws_createGW2.jpeg
* Click on the "Create internet gateway" button which will take you back to the creation screen.
## insert aws_createGW3.jpeg
## insert aws_createGW4.jpeg
--------NOTE--------
The state will say "Detached" which means it is not attached to anything at the moment.
* Attach the gateway to the user's VPC instance which can be done by clicking the "Attach to a VPC"
button at the top right of the page.
* Select the user's VPC from the dropdown and click "Attach internet gateway".
## insert aws_createGW5.jpeg
--------RECAP--------
* We have:
1. Created a "Container" for our use.
2. Created a private IP address for use of the container.
3. Created a range of subnet addresses for use.
4. Created a gateway to talk with the outside world.
--------------------------------
5. Create a Route Table
* In the left banner there is a list of VPC settings, click on "Route Tables".
This will take you to another screen similar to the VPC, Subnet and Gateway creation.
## insert aws_createSubnet.jpeg
* Click on the "Create route table" button and fill in the next page's "Name" with the
user's last name and append "-RouteTable" to the end.
## insert aws_createRT.jpeg
* Using the VPC dropdown, select the user's VPC to attach to and click "Create route table".
## insert aws_createRT2.jpeg
## insert aws_createRT3.jpeg
* Scroll down on the Route Table page and there should only be one route which is set to local,
but it is not attached to any subnets (which can be seen under the "Subnet associations" tab).
## insert aws_createRT4.jpeg
## insert aws_createRT5.jpeg
* Click on the "Edit subnet associations" button to the right of the tabs.
## insert aws_createRT6.jpeg
* Click the available subnet checkbox and then the "Save associations" button.
## insert aws_createRT7.jpeg
## insert aws_createRT8.jpeg
* Scroll back down in the Route Table page to the different tabs section and click the "Edit routes"
button. This needs to be done to add the gateway to the table.
## insert aws_createRT9.jpeg
* Like the other setup/config pages, this will be similar. Click the "Add route" button and then click
into the "Destination" textbox. The dropdown should populate to allow the user to select "0.0.0.0/0".
This is like having a car to go anywhere, where a specific destination is like needing to use the bus.
* Click the "Target" textbox and it will populate a plethura of choices, but for this project we use
the standard "Internet Gateway" which will then populate the user's gateway to click on. Then click
"Save changes".
## insert aws_createRT10.jpeg
## insert aws_createRT11.jpeg
--------------------------------
5. Create a Security Group
* In the left banner there is a list of VPC settings, click on "Security Groups".
This will take you to another screen similar to the VPC, Subnet, Gateway, and Route Tables creation.
## insert aws_createSG.jpeg
## insert aws_createSG2.jpeg
* On the Security Groups settings/config page, input the user's last name with "-SG" appended to it.
* In the "Description" text box input "SSH of trusted networks" or whatever the user decides.
* The VPC is autopopulated, BUT it IS NOT the correct one. Delete the VPC from the textbox and the
ones that are available will populate. Click on the user's VPC.
## insert aws_createSG3.jpeg
* Scroll down to the "Inbound Rules" and click "Add rule". This is going to allow who or whatever the
user wants to connect to the VPC instance which will include Wright State, personal and any others.
## insert aws_createSG4.jpeg
## insert aws_createSG5.jpeg
## insert aws_createSG6.jpeg
--------RECAP--------
* We have:
1. Created a "Routing Table" for the flow of traffic (inbound/outbound).
2. Created a "Security Group" to only allow SSH traffic from trusted sources.
--------------------------------
5. Create a new instance
* Go back to the services page by clicking "Services" at the top left of the AWS screen.
* Click on EC2.
## insert aws_createINST.jpeg
* Scroll down and select "Launce instance".
* Select the first available "Amazon Linux 2 AMI (HVM), SSD Volume Type (because it's free tier eligible
and I don't want to be sad if I were to pick something I haven't tested before).
## insert aws_createINST2.jpeg
## insert aws_createINST3.jpeg
* Leave the checkbox on t2 (because it's free), and click the "Next..." button.
## insert aws_createINST4.jpeg
* Here the user needs to change the "Network" which is set by default to the user's VPC.
## insert aws_createINST5.jpeg
## insert aws_createINST6.jpeg
* Enable the "auto-assign public ip" to allow use of elastic ip addresses so that someone cannot steal (buy)
a set IP address the user specifies.
## insert aws_createINST7.jpeg
* Click the "Next..." button at the bottom right of the screen. The size is preset to 8 Gigs and the volume type
is an SSD which is more than enough for this project.
## insert aws_createINST8.jpeg
* Click the "Next..." button and then click the "Add tag" button. In the first textbox input "Name", then in the
second textbox, input the user's last name and append "-Instance" to the end of it.
## insert aws_createINST9.jpeg
* Click the "Next..." button. Under "Assign a security group, select the "existing" bubble, then the checkbox of
the security group setup by the user earlier.
## insert aws_createINST10.jpeg
## insert aws_createINST11.jpeg
* CLick "Review and Launch" then "Launch". When the next popup comes, the user could change it to have a different
access key, but I'm leaving it the same since I have too many to worry about already.
## insert aws_createINST12.jpeg
## insert aws_createINST13.jpeg
* After all of this, go back to the EC2 Dashboard and click the checkbox of the user's new instance.
## insert aws_createINST14.jpeg
* Click "Actions", "Networking", then "Manage IP addresses". This will take you to a new page which will have a
hyperlink to setup and Elastic IP.
## insert aws_createINST15.jpeg
* Click the "allocate" hyperlink and it will take you to a page with a "Allocate..." button. PRESS IT!!!
## insert aws_createINST16.jpeg
* Leave the top the same, but add the tag using "Name" and the the user's last name with "-EIP" appended to the
end, then click "Allocate" at the bottom.
## insert aws_createINST17.jpeg
## insert aws_createINST18.jpeg
--------END RESULT--------
## insert aws_createEND.jpeg