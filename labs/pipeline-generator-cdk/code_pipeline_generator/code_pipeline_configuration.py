# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. SPDX-License-Identifier: MIT-0

class ContainerPipelineConfiguration:
    AllTest = None
    EndToEndTest = None
    IntegrationTests = None
    LoadTest = None
    LowerEnvironmentDeployment = None
    ProjectName = None
    UnitTest = None

    def __init__(
        self,
        projectName, 
        allTest=True, 
        endToEndTests = False,
        integrationTests = False,
        loadTest = False,
        lowerEnvironmentDeployment = True,
        unitTest=False,
        ):
        self.ProjectName = projectName
        self.AllTest = allTest
        self.UnitTest = unitTest
        self.EndToEndTest = endToEndTests
        self.IntegrationTests = integrationTests
        self.LoadTest = loadTest
    
