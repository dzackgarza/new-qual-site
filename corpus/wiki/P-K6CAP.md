---
schema: qual/card@1
id: P-K6CAP
kind: problem
title: "Let $f, g \\in L^2(\\RR)$. Show that $\\lim _{n \\to \\infty} \\int _{\\RR} f(x) g(x+n) \\,dx = 0$"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Let $f, g \in L^2(\RR)$. Show that
\[
\lim _{n \to \infty} \int _{\RR} f(x) g(x+n) \,dx = 0
\]

:::{.concept}
\envlist
- Cauchy Schwarz: $\norm{fg}_1 \leq \norm{f}_1 \norm{g}_1$.
- Small tails in $L^p$.
:::

:::{.solution}
\envlist

- Use the fact that $L^p$ has small tails: if $h\in L^2(\RR)$, then for any $\eps > 0$, 
\[  
\forall \eps,\, \exists N\in \NN \qst \int_{\abs{x} \geq {N}} \abs{h(x)}^2 \,dx < \eps
.\]

- So choose $N$ large enough so that
\[  
\int_{\norm{x} \geq N}\abs{g(x)}^2 < \eps \\
\int_{\norm{x} \geq N}\abs{f(x)}^2 < \eps \\
.\]

- Then write
\[  
\int_{\RR^d} f(x) g(x+n) \,dx = \int_{\norm{x} \leq N} f(x)g(x+n)\,dx + \int_{\norm{x} \geq N} f(x) g(x+n)\,dx
.\]

- Bounding the second term: apply Cauchy-Schwarz
\[  
\int_{\norm{x} \geq N} f(x) g(x+n)\,dx
\leq 
\qty{ \int_{\norm{x} \geq N} \abs{f(x)}^2}^{1\over 2} \cdot 
\qty{ \int_{\norm{x} \geq N} \abs{g(x)}^2}^{1\over 2}
\leq \eps^{1\over 2} \cdot \norm{g}_2
.\]

- Bounding the first term: also Cauchy-Schwarz, after variable changes
\[  
\int_{\norm{x} \leq N} f(x) g(x+n)\,dx 
&= \int_{-N}^N f(x) g(x+n)\,dx \\
&= \int_{-N+n}^{N+n} f(x-n) g(x)\,dx \\
&\leq \int_{-N+n}^{\infty} f(x-n) g(x)\,dx \\
&\leq \qty{\int_{-N+n}^{\infty} \abs{f(x-n)}^2}^{1\over 2}\cdot \qty{\int_{-N+n}^{\infty} \abs{g(x)}^2}^{1\over 2} \\
&\leq \norm{f}_2 \cdot \eps^{1\over 2}
.\]

- Then as long as $n\geq 2N$, we have
\[  
\int \abs{f(x) g(x+n)} \leq \qty{\norm{f}_2 + \norm{g}_2} \cdot \eps^{1\over 2} 
.\]
:::
