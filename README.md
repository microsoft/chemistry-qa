# ChemistryQA Data

In the real world, there are QA tasks which cannot be solved by end-to-end neural networks and is very difficult to translate the natural language to any kind of formal representation which can be solved. Solving Chemical Calculation Problems is such a QA task. We collect about 5,000 chemical calculation problems from SOCRATIC.ORG, which cover more than 200 topic in chemistry. Unlike other QA datasets, we propose to only label the variable asked and conditions from question stem, but do not label the complex solving process. We name the dataset as ChemistryQA. To encourage other researchers to explore various solutions, we keep this task weakly supervised.


## Data

>Data

>>train.tsv

>>dev.tsv

>>test.tsv

## Evaluation

Please use evaluate.py to evaluate the result as following.
```
python evaluate.py {answer_predict.tsv} {answer_index} {predict_index}
```
where answer_predict.tsv should contain both correct answer and predicted answer by your method, and answer_index and predict_index represent the columne number of correct answer and predicted answer, respectively. 

## Contact us

Please send email to chemistry_qa@microsoft.com.

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

