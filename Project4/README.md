# Project_04 README
Objectives:
* Understand and create a template .yml file that will be uploaded to AWS for automated Cloud Formation
--------------------------------
# Get the template for the automated Cloud Formation
1. Go to the URL below to get the cf-template.yml:
https://github.com/pattonsgirl/Fall2021-CEG3120/blob/main/Projects/Project4/cf-template.yml
* The template provided will be used to upload into Amazon Web Services (AWS) for automated Cloud Formation,
  simlar to Project_03.
--------------------------------
2. Change the "Description" to something relatable.
* When looking at the .yml file, it can be a bit daunting, but all the "key words" are just basically pointers
  for the AWS script that reads it in, to place in the textboxes for building.
* Under the "Description" I have changed mine to read:
![Description](Pictures/Description.jpg)
--------------------------------
3. Change the "Parameters: Keyname"
* The keyname will be what is displayed on the EC2 instance owner's hub.
* If I am correct, this will be what the !REF '<SOMENAME>' will associate connection to, of each node.
![KeyName](Pictures/KeyName.jpg)
--------------------------------
4. Change the "Mappings: AWSRegionUbunut, Server Zone (if necessary) and HVM".
* I have changed my above keywords to:
![Mappings](Pictures/Mappings.jpg)
--------------------------------
5. Change the "Resources: CidrBlock (for the Virtual Private Cloud), and Value".
* I didn't have to change the CidrBlock, but instead of running with the same instance from Project_03 (just
  in case not everyone deleted their stacks) to show that this script actually builds the CF to specification.
* I did however need to change the "Value" keyword from CEG 2350 to reflect CEG 3120.
* Below is my changed Resource block of the .yml file:
![Resources](Pictures/Resources.jpg)
--------------------------------
6. Change the "Subnet: CidrBlock"
* I made mine different again than Project_03 to ensure a real build.
![Subnet](Pictures/Subnet.jpg)
--------------------------------
7. Add in the network that the user will be accessing the instance from with ssh / port 22.
* Mine was added in just below the WSU CIDR:
![SecurityGroup](Pictures/SecurityGroup.jpg)
--------------------------------
8. Change the "Value" tag under the "Name" tag to reflect "CF Instance".
* Below is what my file reflects:
![PublicUbuntuInstance](Pictures/PublicUbuntuInstance.jpg)

