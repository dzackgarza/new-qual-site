---
schema: qual/card@1
id: P-MMAQ-5HMKSRNSGM
kind: problem
title: "Let $f_{n}(x)=a e^{-n a x}-b e^{-n b x} \\quad \\text{ where } 0 < a < b$ Show that $\\sum_{n=1}^{\\infty}\\left|f_{n}\\right| \\text { is not in } L^{1}([0, \\infty), m)$"
classification:
  areas:
  - real-analysis
  topics:
  - series-of-functions
  - integrals
  - convergence-of-functions
  - l1
relations: []
review: draft
---

::: problem
Let
$$
f_{n}(x)=a e^{-n a x}-b e^{-n b x} \quad \text{ where } 0 < a < b.
$$

Show that

a.  $\sum_{n=1}^{\infty}\left|f_{n}\right| \text { is not in } L^{1}([0, \infty), m)$

> Hint: $f_n(x)$ has a root $x_n$.

b.  $$
    \sum_{n=1}^{\infty} f_{n} \text { is in } L^{1}([0, \infty), m) 
    \quad \text { and } \quad 
    \int_{0}^{\infty} \sum_{n=1}^{\infty} f_{n}(x) ~d m=\ln \frac{b}{a}
    $$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $f_n(x) = a e^{-nax} - b e^{-nbx}$ for $x \in [0, \infty)$ with $0 < a < b$. Prove:
(a) $\sum_{n=1}^\infty |f_n| \notin L^1([0, \infty))$;
(b) $\sum_{n=1}^\infty f_n \in L^1([0, \infty))$ with $\int_0^\infty \sum_{n=1}^\infty f_n(x)\,dx = \ln(b/a)$.

<1>1. **Part (a): $\sum_{n=1}^\infty |f_n| \notin L^1([0, \infty))$.**
  <2>1. Find the root $x_n$ of $f_n(x)$:
    $$
    f_n(x) = 0 \iff a e^{-nax} = b e^{-nbx} \iff e^{n(b-a)x} = \frac{b}{a} \iff x_n = \frac{\ln(b/a)}{n(b-a)}.
    $$
    Proof: Since $b > a > 0$, $b/a > 1$ and $b - a > 0$, so $x_n > 0$.
  <2>2. Sign analysis of $f_n(x)$ on $[0, \infty)$:
    For $x \in [0, x_n)$, $f_n(x) < 0$ (since $f_n(0) = a - b < 0$), and for $x \in (x_n, \infty)$, $f_n(x) > 0$.
    Proof: The function $x \mapsto a e^{-nax} - b e^{-nbx} = e^{-nax}(a - b e^{-n(b-a)x})$ has exactly one zero at $x_n$ and is strictly increasing from $a-b < 0$ towards $0$.
  <2>3. Compute $\int_0^\infty |f_n(x)|\,dx$:
    <3>1. An antiderivative of $f_n(x)$ is $F_n(x) = -\frac{1}{n} e^{-nax} + \frac{1}{n} e^{-nbx}$.
      Proof: $F_n'(x) = a e^{-nax} - b e^{-nbx} = f_n(x)$.
    <3>2. $\lim_{x\to\infty} F_n(x) = 0$ and $F_n(0) = 0$.
      Proof: $F_n(0) = -\frac{1}{n} + \frac{1}{n} = 0$.
    <3>3. $\int_0^\infty |f_n(x)|\,dx = -\int_0^{x_n} f_n(x)\,dx + \int_{x_n}^\infty f_n(x)\,dx = -F_n(x_n) + (-F_n(x_n)) = -2 F_n(x_n)$.
      Proof: $\int_0^{x_n} f_n(x)\,dx = F_n(x_n) - F_n(0) = F_n(x_n)$, and $\int_{x_n}^\infty f_n(x)\,dx = 0 - F_n(x_n) = -F_n(x_n)$.
    <3>4. Evaluate $-2 F_n(x_n)$:
      At $x_n = \frac{\ln(b/a)}{n(b-a)}$, we have $e^{-n(b-a)x_n} = a/b$.
      $$
      e^{-nax_n} = \exp\left( -\frac{a}{b-a}\ln\frac{b}{a} \right) = \left(\frac{a}{b}\right)^{\frac{a}{b-a}},
      $$
      $$
      e^{-nbx_n} = \exp\left( -\frac{b}{b-a}\ln\frac{b}{a} \right) = \left(\frac{a}{b}\right)^{\frac{b}{b-a}} = \left(\frac{a}{b}\right) \left(\frac{a}{b}\right)^{\frac{a}{b-a}}.
      $$
      Thus:
      $$
      -F_n(x_n) = \frac{1}{n}\left[ \left(\frac{a}{b}\right)^{\frac{a}{b-a}} - \left(\frac{a}{b}\right)^{\frac{b}{b-a}} \right] = \frac{1}{n}\left(\frac{a}{b}\right)^{\frac{a}{b-a}}\left(1 - \frac{a}{b}\right) = \frac{C_{a,b}}{n},
      $$
      where $C_{a,b} = \left(\frac{a}{b}\right)^{\frac{a}{b-a}}\left(\frac{b-a}{b}\right) > 0$ is a constant independent of $n$.
    <3>5. $\int_0^\infty |f_n(x)|\,dx = \frac{2 C_{a,b}}{n}$.
  <2>4. By Tonelli's Theorem, $\int_0^\infty \sum_{n=1}^\infty |f_n(x)|\,dx = \sum_{n=1}^\infty \int_0^\infty |f_n(x)|\,dx = 2 C_{a,b} \sum_{n=1}^\infty \frac{1}{n} = \infty$.
    Proof: The harmonic series diverges, so the integral of the sum of absolute values is infinite. Thus $\sum_{n=1}^\infty |f_n| \notin L^1([0, \infty))$.

<1>2. **Part (b): $\sum_{n=1}^\infty f_n \in L^1([0, \infty))$ and $\int_0^\infty \sum_{n=1}^\infty f_n(x)\,dx = \ln(b/a)$.**
  <2>1. For each fixed $x > 0$, sum the geometric series:
    $$
    \sum_{n=1}^\infty f_n(x) = a \sum_{n=1}^\infty (e^{-ax})^n - b \sum_{n=1}^\infty (e^{-bx})^n = a \frac{e^{-ax}}{1 - e^{-ax}} - b \frac{e^{-bx}}{1 - e^{-bx}} = \frac{a}{e^{ax} - 1} - \frac{b}{e^{bx} - 1}.
    $$
    Proof: For $x > 0$, $e^{-ax} \in (0, 1)$ and $e^{-bx} \in (0, 1)$, so both geometric series converge absolutely.
  <2>2. Define $S(x) = \frac{a}{e^{ax}-1} - \frac{b}{e^{bx}-1}$ for $x > 0$.
  <2>3. Behavior of $S(x)$ near $x = 0$:
    Using Taylor expansions $e^{tx} - 1 = tx + \frac{1}{2}t^2 x^2 + O(x^3)$:
    $$
    \frac{t}{e^{tx}-1} = \frac{1}{x \left(1 + \frac{1}{2}tx + O(x^2)\right)} = \frac{1}{x} - \frac{t}{2} + O(x).
    $$
    Therefore:
    $$
    S(x) = \left(\frac{1}{x} - \frac{a}{2} + O(x)\right) - \left(\frac{1}{x} - \frac{b}{2} + O(x)\right) = \frac{b-a}{2} + O(x) \quad \text{as } x \to 0^+.
    $$
    In particular, $\lim_{x\to 0^+} S(x) = \frac{b-a}{2}$, so $S(x)$ is bounded on $(0, 1]$.
  <2>4. Behavior of $S(x)$ as $x \to \infty$:
    $S(x) = O(e^{-ax})$ as $x \to \infty$ (since $a < b$, the dominant tail term is $a e^{-ax}$).
    Thus $\int_1^\infty |S(x)|\,dx < \infty$.
  <2>5. $S \in L^1([0, \infty))$.
    Proof: $S$ is continuous on $(0, \infty)$, bounded near $0$, and decays exponentially at $\infty$.
  <2>6. Compute $\int_0^\infty S(x)\,dx$:
    For $0 < \eps < R < \infty$:
    $$
    \int_\eps^R \left( \frac{a}{e^{ax}-1} - \frac{b}{e^{bx}-1} \right) dx = \int_\eps^R \frac{a e^{-ax}}{1 - e^{-ax}}\,dx - \int_\eps^R \frac{b e^{-bx}}{1 - e^{-bx}}\,dx
    $$
    $$
    = \left[ \ln(1 - e^{-ax}) - \ln(1 - e^{-bx}) \right]_\eps^R = \left[ \ln\left(\frac{1 - e^{-ax}}{1 - e^{-bx}}\right) \right]_\eps^R = \ln\left(\frac{1 - e^{-aR}}{1 - e^{-bR}}\right) - \ln\left(\frac{1 - e^{-a\eps}}{1 - e^{-b\eps}}\right).
    $$
    As $R \to \infty$, $\frac{1 - e^{-aR}}{1 - e^{-bR}} \to 1$, so $\ln(1) = 0$.
    As $\eps \to 0^+$, $\frac{1 - e^{-a\eps}}{1 - e^{-b\eps}} = \frac{a\eps + O(\eps^2)}{b\eps + O(\eps^2)} \to \frac{a}{b}$.
    Therefore:
    $$
    \int_0^\infty \sum_{n=1}^\infty f_n(x)\,dx = \lim_{\substack{\eps\to 0^+\\ R\to\infty}} \left( 0 - \ln\frac{a}{b} \right) = \ln\frac{b}{a}.
    $$

<1>3. **Conclusion.**
  Both statements (a) and (b) are fully established. Q.E.D.
:::
