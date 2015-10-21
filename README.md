# Wordfinder

Wordfinder v.0.03
Copyright 2015 Dunwich Type Founders

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Wordfinder was created by James Puckett of Dunwich Type Founders


Wordfinder is a tool that compiles a list of words containing characters drawn from another list. I use it for building font proofs. Characters are found at the beginning, middle, and end of words. Output goes to foundwords.txt

Two lists are used, wordList.txt, a list of words, and charList.txt, a list of characters. Both lists are text files consisting of lines containing a word or character, respectively. Wordfinder works with unicode and characters that are input with multiple characters, such as ದ + ಾ, can be used in charList.txt. Sample wordList and charList files are included.
