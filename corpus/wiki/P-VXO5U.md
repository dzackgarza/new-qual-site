---
schema: qual/card@1
id: P-VXO5U
kind: problem
title: Bernoulli's inequality, and monotonicity and bounds for $(1+1/n)^n$ and $(1+1/n)^{n+1}$
classification:
  areas:
  - real-analysis
  topics:
  - Bernoulli
  - Sequences of Numbers
  - Limits
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

<1>1. $e_n < E_n$.
    Proof: $E_n = (1+1/n)^{n+1} = e_n (1+1/n) > e_n$ since $1+1/n > 1$.
<1>2. Bernoulli's inequality: for $-1 < x$, $(1+x)^n \ge 1 + nx$ for every $n \in \NN$.
    Proof: by induction on $n$. For $n = 1$ it is an equality. If $(1+x)^n \ge 1+nx$, then multiplying by $1+x \ge 0$ (since $x > -1$),
    \[
    (1+x)^{n+1} \ge (1+nx)(1+x) = 1 + (n+1)x + nx^2 \ge 1 + (n+1)x,
    \]
    as $nx^2 \ge 0$.
<1>3. $e_n$ is increasing.
    Proof: with $e_n = ((n+1)/n)^n$,
    \[
    \frac{e_{n+1}}{e_n} = \Big(\frac{n+2}{n+1}\Big)^{n+1}\Big(\frac{n}{n+1}\Big)^n = \Big(1 + \frac{1}{n+1}\Big)\Big(1 - \frac{1}{(n+1)^2}\Big)^n,
    \]
    since $\frac{n(n+2)}{(n+1)^2} = 1 - \frac{1}{(n+1)^2}$. Bernoulli's inequality (<1>2) with $x = -\frac{1}{(n+1)^2}$ gives
    \[
    \Big(1 - \frac{1}{(n+1)^2}\Big)^n \ge 1 - \frac{n}{(n+1)^2} = \frac{n^2+n+1}{(n+1)^2},
    \]
    so
    \[
    \frac{e_{n+1}}{e_n} \ge \frac{n+2}{n+1}\cdot\frac{n^2+n+1}{(n+1)^2} = \frac{(n+2)(n^2+n+1)}{(n+1)^3} = \frac{(n+1)^3 + 1}{(n+1)^3} > 1.
    \]
    Hence $e_{n+1} > e_n$.
<1>4. $E_n$ is decreasing.
    Proof: with $E_n = ((n+1)/n)^{n+1}$,
    \[
    \frac{E_n}{E_{n+1}} = \Big(\frac{n+1}{n}\Big)^{n+1}\Big(\frac{n+1}{n+2}\Big)^{n+2} = \Big(1 + \frac{1}{n(n+2)}\Big)^{n+1}\cdot\frac{n+1}{n+2},
    \]
    since $\frac{(n+1)^2}{n(n+2)} = 1 + \frac{1}{n(n+2)}$. Bernoulli's inequality (<1>2) with $x = \frac{1}{n(n+2)} > 0$ gives
    \[
    \Big(1 + \frac{1}{n(n+2)}\Big)^{n+1} \ge 1 + \frac{n+1}{n(n+2)} = \frac{n^2+3n+1}{n(n+2)},
    \]
    so
    \[
    \frac{E_n}{E_{n+1}} \ge \frac{(n^2+3n+1)(n+1)}{n(n+2)^2} = \frac{n^3 + 4n^2 + 4n + 1}{n^3 + 4n^2 + 4n} > 1.
    \]
    Hence $E_{n+1} < E_n$.
<1>5. $2 < e_n < E_n < 4$ for $n \ge 2$.
    Proof: $e_1 = 2$ and $e_n$ is increasing (<1>3), so $e_n \ge 2$, with $e_2 = 9/4 > 2$; $E_1 = 4$ and $E_n$ is decreasing (<1>4), so $E_n \le 4$, with $E_2 = 27/8 < 4$; and $e_n < E_n$ by <1>1.     Hence $2 < e_n < E_n < 4$ for all $n \ge 2$. (For $n = 1$: $2 = e_1 < E_1 = 4$.)
<1>6. $\lim_{n\to\infty} e_n = \lim_{n\to\infty} E_n$.
    Proof: $e_n$ is increasing and bounded above (by $E_n \le 4$), and $E_n$ is decreasing and bounded below (by $e_n \ge 2$), so both sequences converge. Also $E_n - e_n = e_n/n$, and $0 < e_n/n \le 4/n \to 0$ by <1>5, so the limits are equal.
<1>7. Q.E.D.
:::
