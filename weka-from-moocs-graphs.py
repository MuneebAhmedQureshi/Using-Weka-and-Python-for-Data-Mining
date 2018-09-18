
# coding: utf-8

# ###### Import JVM to run Java Virtual Machine for Weka

# In[1]:


import weka.core.jvm as jvm


# ###### Import Converter to load .arff files

# In[2]:


import weka.core.converters as conv


# ###### Import Evaluaiton and Classifier to use evaluation methods and different classifiers of Weka

# In[3]:


from weka.classifiers import Evaluation, Classifier


# ###### Import Random to seed the  cross-validation methods of Weka

# In[4]:


from weka.core.classes import Random


# ###### Import Weka's tool for plotting classifiers

# In[5]:


import weka.plot.classifiers as plcls


# ###### Import os to use Operating System's Environment Variable "MOOC_DATA" 

# In[6]:


import os


# ###### Starting Java Virtual Machine

# In[7]:


jvm.start(packages=True)


# ###### Loading bodyfat.arff file using Weka's load_any_file method

# In[8]:


data = conv.load_any_file(str(os.environ.get("MOOC_DATA"))+os.sep+"bodyfat.arff")
# or change it to data = conv.load_any_file("bodyfat.arff") if your code and dataset are in same folder

# ###### Setting last attribute of data as the class label

# In[9]:


data.class_is_last()


# ###### Instantiating Weka's Liner Regression classifier

# In[10]:


cls = Classifier(classname="weka.classifiers.functions.LinearRegression", options=["-C","-S","1"])


# ###### Evaluating data

# In[11]:


evl = Evaluation(data)


# ###### Cross Validating data with number of folds set to 10

# In[12]:


evl.crossvalidate_model(cls, data, 10, Random(1))


# ###### Ploting predictions of the evaluation method

# In[13]:


plcls.plot_classifier_errors(evl.predictions, absolute=False, wait=True)


# ###### Stopping the JVM as we don't need it now

# In[14]:


jvm.stop()

