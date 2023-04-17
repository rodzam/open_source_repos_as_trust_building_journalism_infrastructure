# Codebook for "Open-Source Repositories as Trust-Building Journalism Infrastructure: Examining the Use of GitHub by News Outlets to Promote Transparency, Innovation, and Collaboration"

## Project Type

- **News Production Materials**: The repository focuses on providing the code used to generate a user-facing journalistic product or the datasets used for them. Alternatively, the repository contains assets intended to facilitate news production. This category may include providing the HTML code used in an interactive feature published online; hosting data files or other assets associated with a news product; publicly documenting analyses used in a journalistic product (e.g., R or Jupyter notebooks); and storing copies of frequently used resources (e.g., shapefiles used for maps, local Census data, and color swatches). Example: [BuzzFeedNews/2021-05-tx-winter-storm-deaths](https://github.com/BuzzFeedNews/2021-05-tx-winter-storm-deaths/)

- **News Production Technology**: The repository focuses on a technology designed to improve processes closely tied to _news production_. This category may include technological solutions to common workflow challenges or repetitive tasks that news producers face, such as a computer program designed to help a journalist download government data through an API; an automated image tagger that makes it easier for photojournalists to submit their work; a computer script designed to help a designer generate a pre-styled data visualization; a JavaScript library that makes it possible for an interactive designer to add features to a map; or a template for creating a news product. Example: [datadesk/census-data-aggregator](https://github.com/datadesk/census-data-aggregator/)

- **News Distribution Technology**: The repository focuses on a technology designed to improve processes closely tied to _news distribution_. This category may include technologies that improve the serving of content on a particular medium; help reshape content for delivery across multiple media; or add functionality or resiliency to delivery infrastructure (e.g., web servers). The people who interface with these technologies are usually part of the news-producing organization or intermediaries, and _not_ news audiences. Example: [bbc/VideoContext](https://github.com/bbc/VideoContext/)

- **News Interaction Technology**: The repository focuses on a technology designed to improve processes closely tied to _news interaction_ (which includes consumption as well as participation). This category may include a mobile app (e.g., news app for Android or iOS) or digital assistant skill (e.g., Alexa); a JavaScript library loaded by the user that improves their news consumption experience (e.g., by allowing "scrollytelling"); or a chatbot that news audiences can engage with. The people who interface with these technologies are usually news audiences. However, this category may include infrastructural (i.e., server-side) tools that improve the capacity for interaction-related affordances (e.g., a backbone for live user comments). Example: [WSJ/two-step](https://github.com/WSJ/two-step/)

- **General-Purpose Technology**: The repository focuses on a technology that is deemed to be _general purpose_, either by improving processes across more than one of the above stages, improving processes that cannot be readily tied to one of the above stages, or by _explicitly_ aiming to improve processes that go beyond journalism (e.g., stating that it is a general-purpose tool). This category may include a brainstorming tool; a programming library that improves or facilitates access to a general database management system; or a computer script that makes it easier to clean up computer code according to a set of style guidelines. Example: [bustle/radql](https://github.com/bustle/radql/)

- **Education and Events**: The repository focuses on providing educational materials or resources for events. This may include _documenting_ APIs, providing resources for a workshop or hackathon, conveying an organizational set of standards (e.g., code of conduct or programming guide), or offering tutorials for how to use certain technologies. Example: [nytimes/photon-dev_demo](https://github.com/nytimes/photon-dev_demo/)

- **Other**: There is sufficient information about the project to categorize it, but it does not fit into any of the above categories. Example: [VICEMedia/mobile-challenge](https://github.com/VICEMedia/mobile-challenge/)

- **Unclear**: There is insufficient information about this project to determine what it is about. Example: [br/ebconfig](https://github.com/br/ebconfig/)

## Project Scope

- **Minor**: The repository focuses on a project that adds minor functionality to an existing technology (major or minor) created by someone _other than the account-holder_. Alternatively, the project involves an original technology that performs simple tasks or creates modest new affordances. The project may ultimately tackle complex tasks if the original contribution involves little more than linking together technologies created by others. This category may include a computer script that generates a project or directory structure; a program that interfaces with an API to retrieve data or trigger a command; a WordPress plugin that adds simple functionality (e.g., basic contact form); a pipeline that cleans a dataset by passing it through multiple tools created by others; a tool that performs programmatic checks on software, data, or a website to identify errors; a programming library that has a small set of relatively simple functions; or a customization of an existing project (e.g., adding new dialogue options to a Chatbot). Minor technologies generally enable small productivity improvements or introduce small affordances, but do not introduce fundamental changes to an existing technology or way of doing things. Example: [voxmedia/setup-vox-rig](https://github.com/voxmedia/setup-vox-rig/)

- **Major**: The repository focuses on a project that adds major functionality to an existing technology created by someone _other than the account-holder_. Alternatively, the project involves an original technology that performs complex tasks or offers several new affordances. The project may depend on existing technologies provided the original contribution is substantial. This category may include a new data visualization library that includes multiple types of visuals; a new content management system or a plug-in that adds major functionality (e.g., a new content editor for WordPress); or a framework for processing texts involving an original natural language processing engine. Major technologies are generally broadly useful as a stand-alone resource or introduce noteworthy affordances. In some cases, a major project may be broken up into multiple repositories; in such cases, the _core_ components of the project should be coded under this category. Example: [bbc/simorgh](https://github.com/bbc/simorgh/)

- **Other**: There is sufficient information about the project's scope to categorize it, but it does not fit into any of the above categories.

- **Unclear**: There is insufficient information about this project to determine its originality.

- **Not Applicable**: The Project Type was _not_ coded as one of the following: "News Production Technology," "News Distribution Technology," "News Interaction Technology," or "General-Purpose Technology."

## Project Use-Case

- **Internal**: The repository focuses on a project that _primarily_ either targets or benefits an internal audience (i.e., members of the account-holder's organization) or is communicated in terms of its usefulness for, or application by, the account-holder. This may include the open-sourcing of internal development tools and workflow aides that _may_ be useful to others but are not presented with _an emphasis on their external usefulness_. This category may include a computer script that generates templated materials that match organizational conventions; a tool intended to help editors automate organization-specific tasks; or a tool with clear limitations that makes broad adoption unlikely. Extensions to a general-use project that are primarily intended to benefit the account-holder's organization (e.g., creating an organization-specific theme for WordPress) should be coded under this category. Example: [SunSentinel/generator-sunsentinel-interactives](https://github.com/SunSentinel/generator-sunsentinel-interactives/)

- **External**: The repository focuses on a project that is _explicitly_ intended to be reused or repurposed by actors outside the account-holder's organization. Alternatively, it is readily apparent that the project can be broadly useful beyond that organization because of its objectives, design, and documentation. This category may include a programming library or module with general-purpose functionality; a broadly useful plugin for a content management system that is not keyed to an internal challenge; a wrapper that makes it easier to perform broadly useful actions with a general-use programming language; or a tool that automates tasks in ways that have broad utility. These kinds of projects tend to, but need not, be introduced using accessible language that focuses on how general users can make use of the technology. Example: [bloomberg/xcdiff](https://github.com/bloomberg/xcdiff/)

- **Other**: There is sufficient information about the project's use-case to categorize it, but it does not fit into any of the above categories.

- **Unclear**: There is insufficient information about this project to determine its use-case.

- **Not Applicable**: The Project Type was _not_ coded as one of the following: "News Production Technology," "News Distribution Technology," "News Interaction Technology," or "General-Purpose Technology."

## Target Audience

- **Non-Technical**: The repository focuses on a project that has a non-technical target audience, such as a journalist, designer, or general news audience member. This typically involves technologies with pre-built binaries or source code that is fairly easy to compile and execute, and that have functionality that is clearly described or presented in an accessible manner. It also includes technologies that are easy to use by a non-technical audience once deployed (e.g., a JavaScript library that, once deployed by a web developer, simply auto-completes news users' search queries). Projects that require technical know-how but target a non-technical group (e.g., data journalists who use R) should be coded under this category. Example: [DallasMorningNews/fec-downloader](https://github.com/DallasMorningNews/fec-downloader/)

- **Technical**: The repository focuses on a project that has a technical target audience, such as a software developer or system administrator. This typically involves technologies that require compiling _and_ configuration; are only useful within a technical context (e.g., a JavaScript library that adds functions that are mostly useful for programmers or a tool that assists in server management); or have major functionality that is only described or presented in a non-accessible or highly technical manner. Example: [buzzfeed/caliendo](https://github.com/buzzfeed/caliendo/)

- **Other**: There is sufficient information about the project's target audience to categorize it, but it does not fit into any of the above categories.

- **Unclear**: There is insufficient information about this project to determine its target audience.

- **Not Applicable**: The Project Type was _not_ coded as one of the following: "News Production Technology," "News Distribution Technology," "News Interaction Technology," or "General-Purpose Technology."

## Ambient Transparency: Description

- **No**: There is no short, informative description of the project in the 'about' section of the GitHub repository page. Alternatively, there is a description but it is part of a boilerplate that does not clearly apply to the present repository. Example: [guardian/360-pannellum-viewer](https://github.com/guardian/360-pannellum-viewer/)

- **Yes**: There is a short, informative description of the project in the 'about' section of the GitHub repository page. Example: [bbc/ninja-squirrel-image-assets](https://github.com/bbc/ninja-squirrel-image-assets/)

## Ambient Transparency: Links

- **No**: There is no URL associated with the project _and_ there are no _relevant external_ links included within the README file. Alternatively, there is an associated URL or the use of links, but such elements are part of a boilerplate that does not clearly apply to the present repository. Example: [guardian/content-api-dashboard](https://github.com/guardian/content-api-dashboard/)

- **Yes**: There is a URL associated with the project _or_ there are _relevant external_ links included within the README file. Example: [nprapps/oscars](https://github.com/nprapps/oscars/)

## Ambient Transparency: Badges, Releases, or Packages

- **No**: The repository does not include a badge, release or release tag, or published package. Alternatively, such elements do exist but they are part of a boilerplate that does not clearly apply to the present repository. Example: [guardian/content-api-dashboard](https://github.com/guardian/content-api-dashboard/)

- **Yes**: The repository includes a badge, release or release tag, _or_ published package. Example: [theatlantic/thumbor-video-engine](https://github.com/theatlantic/thumbor-video-engine/)

## Disclosure Transparency: Description

- **No**: The README file lacks a project description or offers one that does not provide _a clear sense_ of the contents or purpose of the project. Alternatively, such elements do exist but they are part of a boilerplate that does not clearly apply to the present repository. Example: [axiosvisuals/2018-11-12-california-fires](https://github.com/axiosvisuals/2018-11-12-california-fires/)

- **Yes**: There is a description of the project in the README file that provides a _clear sense_ of the the contents or purpose of the project. Example: [buzzfeed-openlab/colorbot](https://github.com/buzzfeed-openlab/colorbot/)

## Disclosure Transparency: Feature Documentation

- **No**: The README file does not provide a clear listing of the _main_ features of the project. Alternatively, features are described but they are part of a boilerplate that does not clearly apply to the present repository. Example: [bbc/ExCounter](https://github.com/bbc/ExCounter/)

- **Yes**: The README file offers a clear description of how the project works or _clearly lists or describes_ the _major_ features of the project. The meaning of "feature" will vary across projects and should be understood in terms of the project itself. This may include describing affordances in the case of a finished tool; functions in the case of a programming library; variables, limitations, or descriptions of the data source in the case of a dataset; background, limitations, or analytic details in the case of news production materials; and relevant resources in the case of a training or workshop. Features may be described in usage examples. Example: [fivethirtyeight/negro-leagues-player-ratings](https://github.com/fivethirtyeight/negro-leagues-player-ratings/)

## Disclosure Transparency: Usage Documentation

- **No**: The README file does not provide a clear description of how to make use of the project contents. Alternatively, features are described but they are part of a boilerplate that does not clearly apply to the present repository. Example: [cnnlabs/cnn-server](https://github.com/cnnlabs/cnn-server/)

- **Yes**: The README file contains is a clear description of how to make use of the project contents. Usage instructions will vary across projects and should be understood in terms of the project itself. This may include instructions for how to execute a binary or "build" the source code in the case of a finished tool; how to load a module in the case of a programming library; how to load the data or produce a processed version in the case of a dataset; how view or replicate the analysis in case of news production materials (e.g., direct link to Jupyter Notebook); and how to load or make use of the resources in case of a training seminar or workshop. This category should _not_ be selected if the documentation simply lists dependencies but not how to make use of the actual project contents. Example: [The-Politico/django-kanban-budget](https://github.com/The-Politico/django-kanban-budget/)

## Participatory Transparency: General Appeal

- **No**: There is no evident appeal for participation in the README file (or another document clearly linked to from the README). Alternatively, there is an appeal but it is part of a boilerplate that does not clearly apply to the present repository. Example: [bloomberg/constant.js](https://github.com/bloomberg/constant.js/)

- **Yes**: The README file (or another document clearly linked to from the README) contains a general statement or clear heading that invites audiences to participate, such as by encouraging them to open an 'issue' or 'pull request,' ask questions, submit corrections, or otherwise become involved. Example: [newsdaycom/stackpath-php-sdk](https://github.com/newsdaycom/stackpath-php-sdk/)

## Participatory Transparency: Contact Information

- **No**: There is no information about how to contact an individual or group in the README file (or another document clearly linked to from the README), or such information is not connected to any form of participatory appeal. Alternatively, there is an appeal but it is part of a boilerplate that does not clearly apply to the present repository. Example: [associatedpress/ailurus](https://github.com/associatedpress/ailurus/)

- **Yes**: There is information in the README file (or another document clearly linked to from the README) on how to contact an individual or group (e.g., an e-mail address) in order to learn more about the project, ask questions, report problems, or become otherwise involved. That information is tied to a participatory appeal of some sort (e.g., under a heading of "Contributing"). Example: [BuzzFeedNews/zika-data](https://github.com/BuzzFeedNews/zika-data/)

## Participatory Transparency: Details for Contributing

- **No**: There are no specific details for how individuals should contribute in the README file (or another document clearly linked to from the README). Alternatively, there are instructions but they are part of a boilerplate that does not clearly apply to the present repository. Example: [voxmedia/setup-vox-rig](https://github.com/voxmedia/setup-vox-rig/)

- **Yes**: There are specific instructions for how others may/should contribute, or encouragement to contribute in a specific way, in the README file (or another document clearly linked to from the README). This includes a clear link to a contribution guide, instructions on how to register a 'pull request' and clean up code, format an 'issue,' and/or report or correct a discrepancy in the dataset. Example: [bleacherreport/plug_logger_json](https://github.com/bleacherreport/plug_logger_json/)
