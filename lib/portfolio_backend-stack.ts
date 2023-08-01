import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class PortfolioBackendStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here
    const api = new cdk.aws_apigateway.RestApi(this, 'Api', {
      restApiName: 'MyApi',
    });
    const projects = api.root.addResource('projects');
    projects.addMethod('GET', new cdk.aws_apigateway.LambdaIntegration(
                          new cdk.aws_lambda.Function(this, 'Lambda',
                              {runtime: cdk.aws_lambda.Runtime.PYTHON_3_10 , 
                              code:cdk.aws_lambda.Code.fromAsset("src/lambda/") ,
                              handler: "list_projects.handler"})));
    projects.addMethod('POST');
    // example resource
    // const queue = new sqs.Queue(this, 'PortfolioBackendQueue', {
    //   visibilityTimeout: cdk.Duration.seconds(300)
    // });
  }
}
