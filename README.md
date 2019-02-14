# Keywording Benchmark Competition

This repository documents the image keywording benchmark we carried out.



```
Name                   Labels/Image   Precision   Unique Concepts
AWS Rekognition                14.9       0.865              1041
Clarifai                       20.0       0.841              1466
Google Cloud Vision            12.5       0.933              1488
Imagga                         90.1       0.731              4409
Microsoft                      23.6       0.767               559
MobiusLabs mobile high-thresh  13.4       0.934               733
MobiusLabs mobile low-thresh   36.2       0.875              1519
MobiusLabs mobile mid-thresh   26.3       0.899              1224
```

Groundtruth was collected using [Amazons Mechnical Turk](https://www.mturk.com) service. 

Check out [compute evaluation results.ipynb](https://github.com/mobiusml/benchmark_competition/blob/master/compute%20evaluation%20results.ipynb) to find out how we calculated these numbers.
