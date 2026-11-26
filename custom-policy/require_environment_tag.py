from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class S3BucketRequireEnvironmentTag(BaseResourceCheck):
    def __init__(self):
        name = "Ensure S3 bucket has Environment tag (Kebijakan Internal)"
        id = "CUSTOM_AWS_001"
        supported_resources = ["aws_s3_bucket"]
        categories = [CheckCategories.CONVENTION]
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_resources=supported_resources,
        )

    def scan_resource_conf(self, conf):
        tags = conf.get("tags", [{}])
        if isinstance(tags, list) and len(tags) > 0:
            tag_dict = tags[0]
            if isinstance(tag_dict, dict) and "Environment" in tag_dict:
                return CheckResult.PASSED
        return CheckResult.FAILED


check = S3BucketRequireEnvironmentTag()
