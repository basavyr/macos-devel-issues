If you're using a high-end bluetooth headset on your Macbook Pro it's likely your mac is using an audio codec which favors battery efficiency over high quality. This results in a drastic degradation of sound, the SBC codec is the likely culprit, [read more about it here](https://www.soundguys.com/understanding-bluetooth-codecs-15352/).

# Find out what codec you're using

1. Play a song on your headphones
1. Option (⌥) click the Bluetooth button at the top of your screen
   <img width="400" alt="Inspect the Bluetooth Coded" src="https://user-images.githubusercontent.com/1169974/66844914-28ea5480-ef3d-11e9-9faa-22eb52ef37ac.png">
1. If you're using AAC or aptX, you can stop here—those are the highest quality codecs.

# Change your codec to AAC or aptX

_UPDATE: It looks like Apple has silently dropped support for aptX, leaving only AAC_

You'll need to download Apple's Bluetooth Explorer in order to change codecs.

1. Head over to [Apple's Developer Downloads](https://developer.apple.com/download/more/?=additional%20tools)
1. Search for `additional tools` and download `Additional Tools for XCode 11.dmg`
   ![Search for "additional tools"](https://user-images.githubusercontent.com/1169974/66845293-c6458880-ef3d-11e9-945f-85461c0ab605.png)
1. Open the `dmg`, and open `Bluetooth Explorer`
   <img width="1159" alt="Open Bluetooth Explorer" src="https://user-images.githubusercontent.com/1169974/66845593-4966de80-ef3e-11e9-932e-224fb083933b.png">
1. Click on `Tools > Audio Options` and change your audio codec to the following settings:
   - Enable AAC
   - Force use of aptX
   <img width="612" alt="Change your audio codec" src="https://user-images.githubusercontent.com/1169974/66845692-7e733100-ef3e-11e9-809e-12f090f32a19.png">
1. Disconnect your Bluetooth headset, reconnect it, and *while some music is playing,* inspect your codec. It should now show either AAC or aptX.
   
   <img width="400" alt="Your codec should now show AAC/aptX" src="https://user-images.githubusercontent.com/1169974/66845948-fb9ea600-ef3e-11e9-92ac-99878fa81b85.png">
   
# Squeezing the most out of AAC

You can increase the AAC bitrate in `Audio Options` but be sure to keep an eye on the graphs. The retransmission percentage is roughly equivalent to packet loss, and if you increase the bitrate too high your audio will start cutting out:

<img width="400" src="https://user-images.githubusercontent.com/1169974/66846622-0f96d780-ef40-11e9-829d-6450094d27ee.png">

The retransmission rate is a function of distance and interference, and you'll need to disconnect/reconnect on each attempt before you find the sweet spot. 

   