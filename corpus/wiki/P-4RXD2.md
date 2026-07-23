---
schema: qual/card@1
id: P-4RXD2
kind: problem
title: "Let"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Let
\[
f_{n}(x) = a e^{-n a x} - b e^{-n b x} \quad \text{ where } 0 < a < b.
\]

Show that 

a. 
$\sum_{n=1}^{\infty} \left|f_{n}\right|$ is not in $L^{1}([0, \infty), m)$

> Hint: $f_n(x)$ has a root $x_n$.

b.
\[
\sum_{n=1}^{\infty} f_{n} \text { is in } L^{1}([0, \infty), m) 
\qtext{and}
\int _{0}^{\infty} \sum _{n=1}^{\infty} f_{n}(x) \,dm = \ln \frac{b}{a}
\]
:::{.remark}
Not complete.
:::

:::{.solution}
\envlist
:::{.concept}
\envlist
:::

a.

- $f_n$ has a root:
\[  
ae^{-nax} = be^{-nbx} 
&\iff {1\over n} = e^{-nbx} e^{nax} = e^{n(b-a)x}
\iff x = {\ln\qty{a\over b} \over n(a-b)} \definedas x_n
.\]

- Thus $f_n$ only changes sign at $x_n$, and is strictly positive on one side of $x_n$.
- Then
\[  
\int_\RR \sum_n \abs{f_n(x)}\,dx 
&= \sum_n \int_\RR \abs{f_n(x)} \,dx \\
&\geq \sum_n \int_{x_n}^\infty f_n(x) \, dx \\
&= \sum_n {1\over n} \qty{ e^{-bnx} - e^{-anx}\evalfrom_{x_n}^\infty } \\
&= \sum_n {1\over n} \qty{ e^{-bnx_n} - e^{-anx_n} }
.\]

b.

?
:::
