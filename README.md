# botnet-controller
Software for controlling and managing botnets

## Disclaimer

**This project should be used for authorized testing or educational purposes only.**

## What is a Botnet?

A botnet is a number of Internet-connected devices, each of which runs one (or more) bots.

For more info on what a botnet is please vist https://en.wikipedia.org/wiki/Botnet

## Features

Port forwarding is not required and hence server deployment time is quicker and easier

## Getting started?

- Download the software either by cloning it or downloading the zip file.
- Run `controller.exe`, if this is the first time running it, it will download some packages.
- If you are an advance user and already have php, ngrok installed you can edit the source code accordingly and use it, but by default the program will
- itself download all the dependencies.
- You will need an ngrok account(free account will work too) to run the program, it can be done here https://dashboard.ngrok.com/signup

## How?

botnet-controller uses php to host servers locally and uses ngrok to port forward. From there it then grabs the ngrok url and adds it in the botnet malware, which takes orders from the main server (your pc, or wherever the controller is running). The bots then requsts the url and do the task specified to them.

## Note
Shuting down the system will shutdown the server too and you will get a different ngrok URL on hosting the server again. Hence you will lose all the bots 
which use that specific URL as it would no longer be reachable. You will need to keep you device turned on, or if you really want to close it, try 
hibernating it.(it worked once but cannot be guranteed)

## Some additional notes
This software will only work for botnets generated by this software, spreading the malware is to be done by the user.

## Contributors & Maintainers

- canosaur ( [github](https://github.com/canosaur) )
- ZackeryRSmith ( [github](https://github.com/ZackeryRSmith) )


## Screenshots

Screenshots here, if any.

## Licence

Licence here, if set.
<!-- botnet-controller is released under the *none here* License. See [LICENSE](LICENSE) file for more details. -->
