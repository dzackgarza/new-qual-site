---
schema: qual/card@1
id: P-GREPT-39
kind: problem
title: "Domain of $1/g^{-1}(x)$ for $g=x^3+x^2+x+1$ and a value of its inverse"
classification:
  areas: [prelim]
  topics:
  - Inverse Functions
  - Domains
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 39 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Let $g(x) = x^3 + x^2 + x + 1$ be defined for all real $x$. If $f(x) = \frac{1}{g^{-1}(x)}$, which of the following statements is true concerning the domain of $f$ and the value of $f^{-1}(-2)$?

(A) The domain of $f$ is the set of all real $x$ such that $x \neq 0$ or $1$, and $f^{-1}(-2) = -5$.
(B) The domain of $f$ is the set of all real $x$ such that $x \neq 0$ or $1$, and $f^{-1}(-2) = -\frac{1}{5}$.
(C) The domain of $f$ is the set of all real $x$ such that $x \neq -1$, and $f^{-1}(-2) = -\frac{1}{5}$.
(D) The domain of $f$ is the set of all real $x$ such that $x \neq 1$, and $f^{-1}(-2) = -\frac{5}{8}$.
(E) The domain of $f$ is the set of all real $x$ such that $x \neq 1$, and $f^{-1}(-2) = \frac{5}{8}$.
:::

::: {.solution}

::: pf

::: pf-step

The function $g$ is a bijection from $\RR$ to $\RR$.


::: pf-proof

Its derivative is
$$
g'(x)=3x^2+2x+1
=3\left(x+\frac13\right)^2+\frac23>0
$$
for every real $x$, so $g$ is strictly increasing and hence injective.
Moreover, $g(x)\to\pm\infty$ as $x\to\pm\infty$, so continuity and the
intermediate value theorem show that $g$ is surjective. Thus $g^{-1}$ is
defined on all of $\RR$.

:::

:::

::: {.pf-step #s1-2}

The domain of $f$ is
$$
\RR\setminus\{1\}.
$$


::: pf-proof

The quotient
$$
f(x)=\frac1{g^{-1}(x)}
$$
is defined exactly when $g^{-1}(x)\ne0$. Since $g$ is bijective,
$g^{-1}(x)=0$ holds exactly when $x=g(0)$. But
$$
g(0)=1,
$$
so only $x=1$ is excluded.
Moreover, $g^{-1}$ maps $\RR\setminus\{1\}$ bijectively onto
$\RR\setminus\{0\}$, and $t\mapsto1/t$ is a bijection of
$\RR\setminus\{0\}$ with itself. Hence $f$ is bijective from its domain onto
$\RR\setminus\{0\}$, so $f^{-1}(-2)$ is well-defined.

:::

:::

::: {.pf-step #s1-3}

One has
$$
f^{-1}(-2)=\frac58.
$$


::: pf-proof

Let $a=f^{-1}(-2)$. Then $f(a)=-2$, so
$$
\frac1{g^{-1}(a)}=-2
\qquad\Longrightarrow\qquad
g^{-1}(a)=-\frac12.
$$
Applying $g$ gives
$$
a=g\left(-\frac12\right)
=-\frac18+\frac14-\frac12+1
=\frac58.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore the true statement is
$$
\boxed{\text{(E)}}.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives the stated domain in choice (E), and step [](#s1-3){.pf-ref} gives its
stated value of $f^{-1}(-2)$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required choice.

:::

:::

:::
