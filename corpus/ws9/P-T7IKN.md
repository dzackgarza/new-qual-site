---
schema: qual/card@1
id: P-T7IKN
kind: problem
title: "Let $f$ be a holomorphic function in the punctured disk $\\{z : 0 < |z| < 2\\}$\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - singularities
  - holomorphic-functions
relations: []
review: draft
---

::: {.problem title="?"}
Let $f$ be a holomorphic function in the punctured disk $\{z : 0 < |z| < 2\}$ satisfying $$|f(z)| \le \left(\log\frac{1}{|z|}\right)^{100} \text{ in } \{|z| \le 1/2\},$$ $$|f(z)| = 1 \text{ on } |z|=1.$$

a. Show that $f$ has a removable singularity at the origin.
b. Show that if $f(z) \ne 0$ in $|z| < 1$, then $f$ is constant.
c. (Extra credit) True or false, explain.
$$f = \alpha z^n \text{ for } \alpha \in \mathbb{C}, |\alpha| = 1 \text{ and an integer } n \ge 0.$$
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Let $f$ be holomorphic on the punctured disk $\{0 < |z| < 2\}$ with $|f(z)| \le (\log \tfrac{1}{|z|})^{100}$ for $|z| \le \tfrac12$ and $|f(z)| = 1$ on $|z| = 1$. (a) Show $0$ is a removable singularity. (b) Show that if $f(z) \ne 0$ in $|z| < 1$, then $f$ is constant. (c) (Extra credit) True or false: $f = \alpha z^n$ with $|\alpha| = 1$ and $n \ge 0$ an integer.

<1>1. (a) Write the Laurent series $f(z) = \sum_{n \in \ZZ} c_n z^n$ on $0 < |z| < 2$.
    Proof: standard Laurent expansion.

<1>2. $c_n = 0$ for all $n < 0$.
    Proof: by the Cauchy estimate on $|z| = r \le \tfrac12$, $|c_n| \le r^{-n}\qty(\log\tfrac{1}{r})^{100}$ for $n < 0$ (with $-n > 0$), and $r^{-n}(\log \tfrac1r)^{100} \to 0$ as $r \to 0$ (logarithmic growth is slower than any positive power). Hence $c_n = \lim_{r\to 0} = 0$.

<1>3. $0$ is a removable singularity.
    Proof: by <1>2, $f(z) = \sum_{n \ge 0} c_n z^n$ extends holomorphically to $|z| < 2$.

<1>4. (b) Setup: after (a), $f$ is holomorphic on $|z| < 2$, nonzero on $|z| < 1$, and $|f| = 1$ on $|z| = 1$.
    Proof: <1>3 gives holomorphy; the other hypotheses are given.

<1>5. $|f(z)| \le 1$ on $|z| < 1$.
    Proof: the maximum modulus principle on $|z| \le 1$, using $|f| = 1$ on $|z| = 1$ (<1>4).

<1>6. $|f(z)| \ge 1$ on $|z| < 1$.
    Proof: $1/f$ is holomorphic on $|z| < 1$ (as $f \ne 0$ there) and continuous with $|1/f| = 1$ on $|z| = 1$; the maximum modulus principle gives $|1/f| \le 1$, i.e. $|f| \ge 1$.

<1>7. $|f| \equiv 1$ on $|z| < 1$, so $f$ is constant.
    Proof: <1>5 and <1>6 give $|f| \equiv 1$; then $f(D) \subseteq \bd D$, and by the open mapping theorem a nonconstant holomorphic function has open image — a nonempty open set cannot lie in the circle; hence $f$ is constant.

<1>8. (c) The statement is **false** in general.
<2>1. A counterexample: $f(z) = z^{54}\,\frac{z - \tfrac12}{1 - \tfrac12 z}$ satisfies the hypotheses of (a) and has $|f| = 1$ on $|z| = 1$.
    Proof: this is a finite Blaschke product times $z^{54}$: each factor has modulus 1 on $|z| = 1$; it is holomorphic on $|z| < 2$ (pole of $1/(1 - z/2)$ at $z = 2$); and on $|z| \le \tfrac12$, the Blaschke factor has modulus $\le 1$, so $|f(z)| \le |z|^{54} \le (\tfrac12)^{54} < (\log 2)^{100} \le (\log \tfrac1{|z|})^{100}$ (the last inequality since $\log\tfrac1{|z|} \ge \log 2$ there).
<2>2. This $f$ is not of the form $\alpha z^n$.
    Proof: it has a zero at $z = \tfrac12 \ne 0$ (of multiplicity 1), while $\alpha z^n$ has its only zero at $0$.
<2>3. What is true: $f$ is a finite Blaschke product, $f = \alpha z^k\prod_{j=1}^m \frac{z - a_j}{1 - \bar a_j z}$ with $|\alpha| = 1$, $k \ge 0$, $|a_j| < 1$.
    Proof: by (a) $f$ is holomorphic on $|z| < 2$; its zeros in $|z| < 1$ are finite (isolated, cannot accumulate inside $|z| < 2$, and $|f| = 1$ on $|z| = 1$ keeps them away from the boundary). Form the Blaschke product $B$ with the same zeros; then $f/B$ is zero-free with $|f/B| = 1$ on $|z| = 1$, so $|f/B| \equiv 1$ (maximum principle applied to $f/B$ and its reciprocal) and $f/B = \alpha$. The monomial form $\alpha z^n$ holds only when all other zeros are absent.

<1>9. Q.E.D.
    Proof: <1>1–<1>3 prove (a); <1>4–<1>7 prove (b); <1>8 answers (c).
:::
