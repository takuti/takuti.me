---
categories: [Programming]
date: 2021-03-06
keywords: [julia, travis, project, github, actions, workflows, undergone, tokenize,
  tagbot, statistics]
lang: en
recommendations: [/note/juliacon-2019/, /note/recommendation-julia-documenter/, /note/travis-gh-pages-deployment/]
title: 'Moving Julia Project from Travis CI to GitHub Actions #JuliaLang'
---

Thanks to a pull-request "[Install TagBot as a GitHub Action](https://github.com/takuti/Recommendation.jl/pull/12)", which was created by a bot, I realized now is the time to move one of my Julia projects, [Recommendation.jl](https://github.com/takuti/Recommendation.jl), from Travis CI to GitHub Actions.

Since I haven't had enough time to work on the project for a year, migration was not straightforward as I expected. Hence, this post summarizes what I've undergone to get there. As always, I referred to some of the most actively/recently maintained official Julia packages (e.g., [Statistics.jl](https://github.com/JuliaLang/Statistics.jl), [Tokenize.jl](https://github.com/JuliaLang/Tokenize.jl)) to see what is the most 'modern' way to organize a Julia project. 

### Original `.travis.yml`

I've written the following Travis CI configuration more than a year ago:

```yml
language: julia 

os: 
  - linux 
  - osx 

julia:  
  - 0.7 
  - 1.0 
  - nightly 

matrix: 
  allow_failures: 
  - julia: nightly  

notifications:  
  email: false  

after_success:  
  - julia -e 'using Pkg; Pkg.add("Coverage"); using Coverage; Coveralls.submit(process_folder())' 

jobs: 
  include:  
    - stage: "Documentation"  
      julia: 1.0  
      os: linux 
      script: 
        - julia --project=docs/ -e 'using Pkg; Pkg.develop(PackageSpec(path=pwd()));  
                                               Pkg.build("Recommendation"); 
                                               Pkg.instantiate()' 
        - julia --project=docs/ docs/make.jl  
      after_success: skip 
```

The workflow breaks down into three pieces:

1. Unit testing over multiple Julia versions
2. Profiling test coverage
3. Building and publishing a [documentation page](https://takuti.github.io/Recommendation.jl/latest/) to GitHub Pages

### Running a Workflow over multiple Julia versions

First and foremost, what I like about GitHub Actions is the easiness of using a build matrix. 

For every pull-requests onto the master branch, as well as push event to the master with an arbitrary tag, the following workflow executes 3x3=9 jobs for 3 Julia versions and 3 operating systems:

```yml
name: CI
on:
  pull_request:
    branches:
      - master
  push:
    branches:
      - master
    tags: '*'
jobs:
  test:
    name: Julia ${{ matrix.version }} - ${{ matrix.os }} - ${{ matrix.arch }} - ${{ github.event_name }}
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        version:
          - '1.0'
          - '1' # automatically expands to the latest stable 1.x release of Julia
          - 'nightly'
        os:
          - ubuntu-latest
          - macOS-latest
          - windows-latest
        arch:
          - x64
    steps:
      # (actual tasks are defined here)
```

Having a comprehensive build matrix is particularly important for Julia because Julia is one of the rare programming languages that aggressively introduce backward-incompatible changes as the version number grows.

Notice that I dropped Julia 0.7 from the matrix when I switched out the Travis config with GitHub Workflow; considering the stable version is 1.5.3 as of Nov 2020, it's reasonable not to support Julia < 1.0 anymore.

### Testing and reporting coverage

Next, we could leverage **[julia-actions/julia-runtest](https://github.com/julia-actions/julia-runtest)** and **[julia-actions/julia-processcoverage](https://github.com/julia-actions/julia-processcoverage)** as follows:

```yml
jobs:
  test:
    # (define a build matrix - see above)
    steps:
      - uses: actions/checkout@v2
      - uses: julia-actions/setup-julia@v1
        with:
          version: ${{ matrix.version }}
          arch: ${{ matrix.arch }}
      - uses: actions/cache@v1
        env:
          cache-name: cache-artifacts
        with:
          path: ~/.julia/artifacts
          key: ${{ runner.os }}-test-${{ env.cache-name }}-${{ hashFiles('**/Project.toml') }}
          restore-keys: |
            ${{ runner.os }}-test-${{ env.cache-name }}-
            ${{ runner.os }}-test-
            ${{ runner.os }}-
      - uses: julia-actions/julia-buildpkg@v1
      - uses: julia-actions/julia-runtest@v1
      - uses: julia-actions/julia-processcoverage@v1
      - uses: codecov/codecov-action@v1
        with:
          file: lcov.info
```

As long as your repository is registered to [Codecov.io](https://app.codecov.io/gh/takuti/Recommendation.jl), test coverage is automatically reported in a pull-request. See [this comment](https://github.com/takuti/Recommendation.jl/pull/19#issuecomment-786509818) as an example.

### Documenting and hosting on GitHub Pages

Finally, we can define a dedicated job for building and publishing a documentation page using [Documenter.jl](https://github.com/JuliaDocs/Documenter.jl). 

Luckily, there is an official step-by-step guide: **[Hosting Documentation](https://juliadocs.github.io/Documenter.jl/stable/man/hosting/#GitHub-Actions)**, and the definition of the job looks like:

```yml
jobs:
  docs:
    name: Documentation
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: julia-actions/setup-julia@v1
        with:
          version: '1'
      - run: |
          julia --project=docs -e '
            using Pkg
            Pkg.develop(PackageSpec(path=pwd()))
            Pkg.instantiate()'
      - run: julia --project=docs docs/make.jl
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          DOCUMENTER_KEY: ${{ secrets.DOCUMENTER_KEY }}
          DOCUMENTER_DEBUG: true
```

`secrets.GITHUB_TOKEN` is automatically set by GitHub Workflow. 

Meanwhile, `secrets.DOCUMENTER_KEY` can be generated as explained in **[Authentication: SSH Deploy Keys](https://juliadocs.github.io/Documenter.jl/stable/man/hosting/#travis-ssh)** and be configured as a custom GitHub repository secret at: `https://github.com/{user}/{repository}/settings/secrets/`.

It is important to note that we should accordingly update [TagBot Workflow](https://github.com/takuti/Recommendation.jl/blob/master/.github/workflows/TagBot.yml):

```diff
  - uses: JuliaRegistries/TagBot@v1
    with:
      token: ${{ secrets.GITHUB_TOKEN }}
+     ssh: ${{ secrets.DOCUMENTER_KEY }}
```

Moreover, in case you're using an old version of Documenter.jl like me, you probably need to update the version in `docs/Project.toml` first of all because GitHub Actions are supported since Documenter.jl 0.24:

```diff
  Documenter = "e30172f5-a6a5-5a46-863b-614d45cd2de4"

  [compat]
- Documenter = "~0.20"
+ Documenter = "0.24" 
```

That's all, and [here](https://github.com/takuti/Recommendation.jl/tree/master/.github/workflows) is a complete set of GitHub Actions Workflows for my Julia project.