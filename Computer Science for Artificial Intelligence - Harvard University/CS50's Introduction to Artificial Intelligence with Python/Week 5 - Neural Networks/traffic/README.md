**Traffic** <br>
Assignement: Write an AI to identify which traffic sign appears in a photograph.

---

Here is the structure for the very first model I ran:
- My convolutional layer had 32 filters using a 3x3 kernel, a `relu` activation function and the input shape required in the specifications,
- The model had also one max-pooling layer with a pool_size of 2x2,
- One flatten layer,
- One hidden layer with 64 units and a `relu` activation function,
- One dropout layer with a 50% dropout rate,
- And the output layer with `NUM_CATEGORIES` units
- Compile loss : binary_crossentropy and a `softamx` activation function.

With these parameters, the results were pretty satisfying (for a first attempt): I obtained a 0.0232 loss and an accuracy of 0.9181. 
To be noted: the accuracy for the first epoch was very low (0.1555) but it ended up to be much higher (0.7418) for the last and tenth epoch. 

I then decided to add more filters to my convolutional layer and added 32 more, for a total of 64 filters.
The results were encouraging: the loss rate was rather similar (0.0238), and I obtained a higher accuracy rate (0.9276).

For my third attempt, I went on and doubled the number of filters for the first layer and ended up with 128 filters in total.
This time however, the results were not very compelling. The loss was increasing (not drastically, thankfully), and the accuracy was pretty much the same. 

I thus reset the number of filters for the convolutional layer to 64, and I added two layers to apply convolution and pooling again. Here the loss dropped to 0.0183 and the accuracy went up to 0.9549. The downside though is that, as layers were added, this version of the model required more time to process. It went from 2ms/step with the previous version to 3ms/step with this version. 

I decided to try and add two more layers, to apply convolution and pooling a third time. The results were even better (the loss was 0.0093 while the accuracy was 0.9630). But this model becomes costly. The average step time went up to 5ms/step.

I then decided to change the number of units for my hidden layer to 128 (it was 64 originally). These settings allowed me the divide the loss by more than 2 (although at this point, it is dangerously getting too close to 0.0000), and the accuracy went up to 0.9830. Such results were very satisfying considering that these parameters didn't have the negative effect of increasing the average step time, which remained 5ms/step.

I went on and doubled the number of units for the hidden layer to see if it could benefit the accuracy of the model. And it was a success! The loss was 0.0031 while the accuracy was 0.9859 and the average step time was still 5ms/step.

At this point, I figured I wouldn't be able to obtain much better results, as I was alread afraid to be facing overfitting.

But still, I tried running my model with an additional hidden layer that had the exact same parameters as the first one (i.e. 256 filters and a 50% dropout rate). The loss was even lower (0.0029) but the accuracy was not as good (0.9808).

I removed the newly created hidden layer and I changed the number of filters of the original hidden layer, which was now 512. But with this 9th attempt, the results were not compelling either. The loss had slightly incread (0.0035) while the accuracy was still not as good as the best result we got. Additionally, the average step time had gone up to 6ms/step.

Lastly, I took a look at my output layer and decided to try to train my model using a different type of activation function for this layer. Originally, it was a softmax type of activation function, which I changed to sigmoid. The loss went up (0.0041) and the accuracy went down (0.9783). 

It thus seemed I'd obtained the best results with the parameters and settings used in attempt #7:
- A convolutional layer with 64 filters, a 3x3 kernel, a `relu` activation function and an input_shape equals to (IMG_WIDTH, IMG_HEIGHT, 3),
- A max-pooling layer, using a 2x2 pool size,
- The same 2 layers repeated twice to apply convolution and pooling 3 times in total,
- A flatten layern
- A hidden layer with 256 filters, a `relu` activation function and a dropout rate of 50%,
- An output layer with `NUM_CATEGORIES` units and a `softmax` activation function.

This was very interesting to do and trying out different parameters is definetly one of the most exciting parts of the machine learning process!
Here's the link to my live demonstration of the model on Youtube: https://youtu.be/DIBX8mnMfFM
