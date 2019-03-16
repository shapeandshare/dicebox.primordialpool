The Primordial Pool
===================

Overview
--------
Based on the defined hyper-parameters evolutionary optimization is employed to select for successive generations of neural networks.  

```
    python ./primordialpool.py
```

### Production Deployment

**Docker Container**

The recommended way to run the service is by using the official provided docker container.
The container should be deployed to a Docker Swarm as a service.

**Example**
```
docker run \
dicebox.primordialpool
```

How to apply rolling updates of the service within the swarm:
```
docker service update --image shapeandshare/dicebox.primordialpool:latest primordialpool
```

In the examples above the Docker Swarm was deployed to AWS and had the Cloudstor:aws plugin enabled and active.
The primorial pool containers will store and read data from the shared storage.

**Global shared Cloudstor volumes mounted by all tasks in a swarm service.**

The below command is an example of how to create the shared volume within the docker swarm:
```
docker volume create -d "cloudstor:aws" --opt backing=shared dicebox
```

References
----------

[Matt Harvey](https://github.com/harvitronix) thank you, for without you dicebox would not be.  Much of the current implementation of dicebox comes from Matt's project below.  I originally forked Matt's work and used it until it outgrew what it was.

* [Blog Post](https://blog.coast.ai/lets-evolve-a-neural-network-with-a-genetic-algorithm-code-included-8809bece164) & [Code](https://github.com/harvitronix/neural-network-genetic-algorithm)

**Projects that I worked with heavily during prior implementations of dicebox**

* [Tensorflow & the 'slim' samples](https://github.com/tensorflow/tensorflow)
* [Tensorflow models](https://github.com/tensorflow/models)
* [EasyTensorflow](https://github.com/calvinschmdt/EasyTensorflow)

**Additional projects used here, or were reference material for dicebox**

* D20 Roll Fairness Evaluation | [Blog Post](http://www.markfickett.com/stuff/artPage.php?id=389) & [Code](https://github.com/markfickett/dicehistogram)
* Keras | [Site](https://keras.io/) & [Code](https://github.com/fchollet/keras)
* [JPG-and-PNG-to-MNIST](https://github.com/gskielian/JPG-PNG-to-MNIST-NN-Format)


Contributing
------------
1. Fork the repository on Github
2. Create a named feature branch (like `add_component_x`)
3. Write your change
4. Write tests for your change (if applicable)
5. Run the tests, ensuring they all pass
6. Submit a Pull Request using Github

License and Authors
-------------------
MIT License

Copyright (c) 2017-2019 Joshua C. Burt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.