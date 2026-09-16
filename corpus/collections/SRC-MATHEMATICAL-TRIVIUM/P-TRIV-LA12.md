---
schema: qual/card@1
id: P-TRIV-LA12
kind: problem
title: 'Wronskian: Abel''s formula, change of variables and scaling'
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 12, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: problem
Consider the Wronskian

$$
W _ { x } ( y _ { 1 } , . . . , y _ { n } ) = \operatorname * { d e t } \left[ \begin{array} { c c c c c c } { y _ { 1 } } & { y _ { 2 } } & { y _ { 3 } } & { . . . } & { y _ { n } } \\ { y _ { 1 } ^ { \prime } } & { y _ { 2 } ^ { \prime } } & { y _ { 3 } ^ { \prime } } & { . . . } & { y _ { n } ^ { \prime } } \\ { y _ { 1 } ^ { \prime \prime } } & { y _ { 2 } ^ { \prime \prime } } & { y _ { 3 } ^ { \prime \prime } } & { . . . } & { y _ { n } ^ { \prime \prime } } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { y _ { 1 } ^ { ( n - 1 ) } } & { y _ { 2 } ^ { ( n - 1 ) } } & { y _ { 3 } ^ { ( n - 1 ) } } & { . . . } & { y _ { n } ^ { ( n - 1 ) } } \end{array} \right] ,\tag{5}
$$

where $y _ { 1 } , . . . , y _ { n }$ are $C ^ { n - 1 }$ functions of x.

(a) Let $y _ { 1 }$ and $y _ { 2 }$ be two solutions of the differential equation $y ^ { \prime \prime } - a y ^ { \prime } - b y = 0$ where a and b are some known functions of x. Find an expression for the Wronskian $W _ { x } ( y _ { 1 } , y _ { 2 } )$ depending on a and b. Then, show that if one of the solutions, say, $y _ { 1 }$ , is known, then another can be found from the first order equation $y _ { 1 } ^ { \prime } - { \frac { y _ { 2 } ^ { \prime } } { y _ { 2 } } } y _ { 1 } + { \frac { W _ { x } ( y _ { 1 } , y _ { 2 } ) } { y _ { 2 } } } = 0$

(b) Show that under change of variable $x \to t ( x )$ the Wronskian transforms as follows,

$$
W _ { x } ( y _ { 1 } , . . . , y _ { n } ) = \left( \frac { d t } { d x } \right) ^ { \frac { n ( n - 1 ) } { 2 } } W _ { t } ( y _ { 1 } , . . . , y _ { n } ) .\tag{6}
$$

(c) Show that $W _ { x } ( y y _ { 1 } , . . . , y y _ { n } ) = y ^ { n } W _ { x } ( y _ { 1 } , . . . , y _ { n } )$ , where y is some $C ^ { n - 1 }$ function.
:::
