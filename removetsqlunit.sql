-- Drop procedures if they exist
IF OBJECT_ID(N'[dbo].[tsu_AssertEqual]', N'P') IS NOT NULL
    DROP PROCEDURE [dbo].[tsu_AssertEqual];
GO

IF OBJECT_ID(N'[dbo].[tsu_describe]', N'P') IS NOT NULL
    DROP PROCEDURE [dbo].[tsu_describe];
GO

IF OBJECT_ID(N'[dbo].[tsu__private_addError]', N'P') IS NOT NULL
    DROP PROCEDURE [dbo].[tsu__private_addError];
GO

IF OBJECT_ID(N'[dbo].[tsu__private_addFailure]', N'P') IS NOT NULL
    DROP PROCEDURE [dbo].[tsu__private_addFailure];
GO

IF OBJECT_ID(N'[dbo].[tsu__private_createTestResult]', N'P') IS NOT NULL
    DROP PROCEDURE [dbo].[tsu__private_createTestResult];
GO

IF OBJECT_ID(N'[dbo].[tsu__private_showTestResult]', N'P') IS NOT NULL
    DROP PROCEDURE [dbo].[tsu__private_showTestResult];
GO

IF OBJECT_ID(N'[dbo].[tsu_error]', N'P') IS NOT NULL
    DROP PROCEDURE [dbo].[tsu_error];
GO

IF OBJECT_ID(N'[dbo].[tsu_failure]', N'P') IS NOT NULL
    DROP PROCEDURE [dbo].[tsu_failure];
GO

IF OBJECT_ID(N'[dbo].[tsu_runTestSuite]', N'P') IS NOT NULL
    DROP PROCEDURE [dbo].[tsu_runTestSuite];
GO

IF OBJECT_ID(N'[dbo].[tsu_runTests]', N'P') IS NOT NULL
    DROP PROCEDURE [dbo].[tsu_runTests];
GO

IF OBJECT_ID(N'[dbo].[tsu_showTestResults]', N'P') IS NOT NULL
    DROP PROCEDURE [dbo].[tsu_showTestResults];
GO

-- Drop tables if they exist
IF OBJECT_ID(N'[dbo].[tsuActiveTest]', N'U') IS NOT NULL
    DROP TABLE [dbo].[tsuActiveTest];
GO

IF OBJECT_ID(N'[dbo].[tsuErrors]', N'U') IS NOT NULL
    DROP TABLE [dbo].[tsuErrors];
GO

IF OBJECT_ID(N'[dbo].[tsuFailures]', N'U') IS NOT NULL
    DROP TABLE [dbo].[tsuFailures];
GO

IF OBJECT_ID(N'[dbo].[tsuLastTestResult]', N'U') IS NOT NULL
    DROP TABLE [dbo].[tsuLastTestResult];
GO

IF OBJECT_ID(N'[dbo].[tsuTestResults]', N'U') IS NOT NULL
    DROP TABLE [dbo].[tsuTestResults];
GO
