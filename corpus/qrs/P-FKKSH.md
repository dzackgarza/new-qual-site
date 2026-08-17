---
schema: qual/card@1
id: P-FKKSH
kind: problem
title: "For $n\\in \\NN$, define $e_{n} = \\left (1+ {1\\over n} \\right)^{n} \\qtext{and} E_{n} = \\left( 1+ {1\\over n} \\right)^{n+1}$ Show that $e_n < E_n$, and prove Bernoulli's\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - bernoulli
  - sequences-of-numbers
  - limits
relations: []
review: draft
solved: true
---

::: problem
For $n\in \NN$, define
\[
e_{n} = \left (1+ {1\over n} \right)^{n} 
\qtext{and}
E_{n} = \left( 1+ {1\over n} \right)^{n+1}
\]

Show that $e_n < E_n$, and prove Bernoulli's inequality:
\[
(1+x)^n \geq 1+nx && -1 < x < \infty  ,\,\, n\in \NN
.\]


Use this to show the following:

1. The sequence $e_n$ is increasing.
2. The sequence $E_n$ is decreasing.
3. $2 < e_n < E_n < 4$.
4. $\lim _{n \to \infty} e_{n} = \lim _{n \to \infty} E_{n}$.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. $e_n < E_n$ for every $n$.
    Proof: $E_n = \left(1 + \frac{1}{n}\right)^{n+1} = e_n\left(1 + \frac{1}{n}\right) > e_n$ since $1 + 1/n > 1$.

<1>2. Bernoulli's inequality: for $-1 < x < \infty$ and $n \in \NN$, $(1 + x)^n \ge 1 + nx$.
    <2>1. The case $n = 1$ is an equality.
        Proof: $(1+x)^1 = 1 + x$.
    <2>2. Induction step: if $(1+x)^n \ge 1 + nx$, then $(1+x)^{n+1} \ge 1 + (n+1)x$.
        Proof: $(1+x)^{n+1} = (1+x)^n(1+x) \ge (1+nx)(1+x)$, valid because $1 + x > 0$ (as $x > -1$); expanding: $(1+nx)(1+x) = 1 + (n+1)x + nx^2 \ge 1 + (n+1)x$ since $nx^2 \ge 0$.
    <2>3. Q.E.D.
        Proof: <2>1 and <2>2.

<1>3. The sequence $e_n$ is increasing.
    <2>1. $\frac{e_{n+1}}{e_n} = \frac{n+2}{n+1}\left(1 - \frac{1}{(n+1)^2}\right)^n$.
        Proof: $\frac{e_{n+1}}{e_n} = \frac{(1 + 1/(n+1))^{n+1}}{(1 + 1/n)^n} = \left(\frac{n+2}{n+1}\right)^{n+1}\left(\frac{n}{n+1}\right)^n = \frac{n+2}{n+1}\left(\frac{n(n+2)}{(n+1)^2}\right)^n = \frac{n+2}{n+1}\left(1 - \frac{1}{(n+1)^2}\right)^n$.
    <2>2. $\left(1 - \frac{1}{(n+1)^2}\right)^n \ge 1 - \frac{n}{(n+1)^2}$.
        Proof: Bernoulli's inequality (<1>2) with $x = -\frac{1}{(n+1)^2} > -1$.
    <2>3. $\frac{e_{n+1}}{e_n} \ge \frac{n+2}{n+1}\left(1 - \frac{n}{(n+1)^2}\right) = \frac{(n+2)(n^2+n+1)}{(n+1)^3} = 1 + \frac{1}{(n+1)^3} > 1$.
        Proof: <2>1, <2>2, and direct algebra ($(n+2)(n^2+n+1) = (n+1)^3 + 1$).
    <2>4. Q.E.D.
        Proof: <2>3 gives $e_{n+1} > e_n$.

<1>4. The sequence $E_n$ is decreasing.
    <2>1. $\frac{E_n}{E_{n+1}} = \frac{n+1}{n+2}\left(1 + \frac{1}{n(n+2)}\right)^{n+1}$.
        Proof: $\frac{E_n}{E_{n+1}} = \frac{(1+1/n)^{n+1}}{(1+1/(n+1))^{n+2}} = \left(\frac{n+1}{n}\right)^{n+1}\left(\frac{n+1}{n+2}\right)^{n+2} = \frac{n+1}{n+2}\left(\frac{(n+1)^2}{n(n+2)}\right)^{n+1} = \frac{n+1}{n+2}\left(1 + \frac{1}{n(n+2)}\right)^{n+1}$.
    <2>2. $\left(1 + \frac{1}{n(n+2)}\right)^{n+1} \ge 1 + \frac{n+1}{n(n+2)}$.
        Proof: Bernoulli's inequality (<1>2) with $x = \frac{1}{n(n+2)} > 0$.
    <2>3. $\frac{E_n}{E_{n+1}} \ge \frac{n+1}{n+2}\left(1 + \frac{n+1}{n(n+2)}\right) = \frac{(n+1)(n^2+3n+1)}{n(n+2)^2} = 1 + \frac{1}{n(n+2)^2} > 1$.
        Proof: <2>1, <2>2, and direct algebra ($(n+1)(n^2+3n+1) = n(n+2)^2 + 1$).
    <2>4. Q.E.D.
        Proof: <2>3 gives $E_n > E_{n+1}$.

<1>5. $2 \le e_n < E_n \le 4$ for all $n$, with strict inequalities for $n \ge 2$.
    <2>1. $e_n \ge e_1 = 2$ and $E_n \le E_1 = 4$.
        Proof: $e_n$ increasing by <1>3; $E_n$ decreasing by <1>4; $e_1 = 2$ and $E_1 = 4$.
    <2>2. $e_n < E_n$ by <1>1, and for $n \ge 2$: $e_n > e_1 = 2$ and $E_n < E_1 = 4$.
        Proof: strict monotonicity in <1>3 and <1>4.
    <2>3. Q.E.D.
        Proof: <2>1 and <2>2.

<1>6. $\lim_{n\to\infty} e_n = \lim_{n\to\infty} E_n$.
    <2>1. Both sequences converge.
        Proof: $e_n$ is increasing and bounded above (by $E_n \le 4$); $E_n$ is decreasing and bounded below (by $e_n \ge 2$).
    <2>2. $E_n - e_n = \frac{e_n}{n} \to 0$.
        Proof: $E_n = e_n(1 + 1/n)$ by definition, and $0 < e_n/n \le 4/n \to 0$ by <1>5.
    <2>3. Q.E.D.
        Proof: <2>1 and <2>2 imply the limits are equal (their difference tends to $0$).
:::
