# ChemistryQA Data
ChemistryQA is a complex QA task which cannot be solved by end-to-end neural networks. To answer chemical questions, machines need to understand questions, apply chemistry and math knowledge, and do calculation and reasoning. ChemistryQA contains about 4500 questions covering around 200 chemistry topics, which are collected from https://socratic.org/chemistry. 

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

Please send email to chemistry_qa@microsoft.com if you have any problem.

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

## License

[Computational Use of Data Agreement](https://github.com/microsoft/Computational-Use-of-Data-Agreement).
