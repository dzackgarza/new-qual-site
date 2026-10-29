---
schema: qual/card@1
id: FE-ISVDM
kind: example
title: $A^n = B^n$ does not imply $A = B$ for matrices
prompts:
- Does $A^n=B^n$ imply $A=B$?
- For matrices, does $A^n=B^n\implies A=B$?
classification:
  areas:
  - algebra
  topics:
  - Matrices
  - Counterexamples
relations: []
review: draft
---

::: {.example}
For square matrices $A,B$ and $n\ge2$, $A^n=B^n$ does not imply $A=B$.
In $\Mat_2(\RR)$, let $\theta\coloneqq 2\pi/n$ and
$$
R=\matt{\cos\theta}{-\sin\theta}{\sin\theta}{\cos\theta},
$$
the rotation of $\RR^2$ through $\theta$.
Then $R^n$ is the rotation through $2\pi$, so $R^n=I=I^n$, but $R\ne I$ because $0<\theta\leq\pi$.
:::

::: {.remark title="Variations"}
For $n=2$ the rotation is $R=-I$, and other witnesses are common.
The swap matrix $M=\matt 0 1 1 0$ satisfies $M^2=I=I^2$ with $M\neq I$.
The matrix $A=\matt 0 1 {-1} 0$ satisfies $A^2=-I=(-A)^2$ with $A\neq -A$, so squaring is not injective even away from $\pm I$.
:::
