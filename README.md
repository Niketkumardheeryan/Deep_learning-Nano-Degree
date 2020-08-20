# Deep_learning-Nano-Degree

## Abstract 

### Advance  Deep learning 

# Topics covered
### Introduction of Anaconda or jupyter Notebook
   #### Jupyter Notebook is a web app
   * Magic word like % or %%
   * can be accessed any where by using cloud computing .
      
   * & Anaconda is a
     >> Software distribution, package or Environment manager.\
     
     
     
### Neural networks Fundamentals 
    >>Perceptron algorithm 
    >>Error function 
    >>Discrete(Step funcion) or continuous(sigmoid) Error functions
    >>Softmax error function for multiclass classification
    #####  Gradient Descent Algorithm    
           GDA= - learning rate * gradient 
            In simple words - ve slope for improve error function
            
      #### Cross Entropy = -(sigma of ln(probability of predictions))
                           it shows how accurate a neural network workikng .
                                 
     #### Feed forwardation -->> process to take inputs and get final output 
     
     #### Backpropagation  is the central mechanism by which neural networks learn.
   
### Implementation of Gradient Descent with Multilayer perceptron

### Training of neural networks 

    overfitting vs underfitting ->> *in overfitting* training error is low but Testing error is high, *in underfittinng* Both errors
     are high.
     
     1./* Technique to remove overfitting*/ ->> Regularization  (L1,L2)
     2.[Dropout] : in this technique we drop some nodes which has more weight already or train only less
                   Weight contain nodes. 
* [Types of Gradient descent]:
  * 1.Batch GD : take all data point in each epoch
  * 2. Stochastic GD : Take different data-sets in each epoch
  * 3.Mini Batch Gd : SGD + BGD

## Introduction to Pytorch 
 * A DL framework develope by FB Ai research team
 * Faster than Tensorflow 
 * Neural networks from scratch 
 * Torchvision library for importing different types of Vision data set 
    Ex. MNSIT digit Recognition.. 🤗 
     
## CNN

  * Better than MLP ,beacause In cnn layer each node is not connected to every node of Next layer Only Required ones  
  * 4 types of filters used in cnnn layer
  * Applications: Style transfer, Transfer learning as VGG16,VGG19 trained with Image net dataset
 ### Transfer learning 
   *pretrained models
   ### Structure of code in Pytorch 
       CNN layer -relu- > Max pooling - - >cNN layer-relu-pooling... + 3 normal layer Then apply softmax or any other activation function

## RNN
  Recurrent Neural network introduce memory in neural network  
 * Specially working area -Text processing Chat bot,Shri,GOOgle assistant
 * *problem -Gradient vanishing
 * LSTM  Resolve this problem
 * LSTM used 4 *Gates in model 

## GAN
 * Generator Adversial Network "Produce fake images based on given images or data"
 * GAN uses 2 models "Discriminator + Generator" 
 * Discriminator is a simple network classofy 
     real images or produce real images
     but Generator produce Fake images By creating Errors in Model.

  ### DCGAN
## MOdel DEPLOY

## contacts
