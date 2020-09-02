# TDD Rediscovered - ProgrammerTests

## What is this?

This is an implementation of [Conway's Game of Life](https://github.com/iancooper/GameOfLife), used to support my course: TDD Rediscovered.

It is public to support students of that course reviewing the code used.

## The Rules

The code was created as a kata, using the following rules:

* We are writing [Programmer Tests](https://wiki.c2.com/?ProgrammerTest). A failing test tells us that the last edit to the source is the source of an issue

* The prompt to write a test is a new requirement. We assume that we obtained these when elaborating the story with the customer.

* When we discover that we need new collaborators by refactoring we ask: are they part of our public interface or an implementation detail. We don’t test implementation details

## Branches

The master branch is the output of the original kata.

There are two branches:

* Refactoring Steps: The commits here show various refactorings, which may be well advised (removing duplication) or ill-advised (intrdocuing a class hierachy). Their goal is to show that we can refactor details, without writing new tests around those details, if they are private.
* Clean Architecture: This branch makes the code runnable. It seeks to demonstrate that the idea of Clean Architecure - adapaters, use cases, and entities - can be implemented straightforwardly, and let us separate the 'hard to test' concepts easily. Ultimately 'Game' here would be a good test target to drive TDD.


