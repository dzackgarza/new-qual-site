---
schema: qual/card@1
id: P-NBSTW
kind: problem
title: Power series of $\tan z$ via geometric-series inversion
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Trigonometry
  - Laurent Series
relations: []
review: draft
---

::: {.exercise}
Laurent expand $\tan(z)$ at $0$ using this method to compute $1/\cos(z)$ and taking the product $\sin(z) \cdot {1\over \cos(z)}$.
:::

::: {.solution}

Example.
To find the coefficients of $z^m$ for $m \leq 5$ in the power series expansion of $\tan z=\sin z / \cos z$ about $z=0$, we calculate as follows, again using the notation $\mathcal{O}\left(z^m\right)$ for terms involving powers $z^k$ for $k \geq m$ :
\[
\begin{aligned}
\frac{1}{\cos z} & =\frac{1}{1-\left(z^2 / 2 !\right)+\left(z^4 / 4 !\right)+\mathcal{O}\left(z^6\right)} \\
& =1+\left(\frac{z^2}{2 !}-\frac{z^4}{4 !}+\mathcal{O}\left(z^6\right)\right)+\left(\frac{z^2}{2 !}-\frac{z^4}{4 !}+\mathcal{O}\left(z^6\right)\right)^2+\mathcal{O}\left(z^6\right) \\
& =1+\frac{1}{2} z^2+\frac{5}{24} z^4+\mathcal{O}\left(z^6\right)
\end{aligned}
\]
so that
\[
\begin{aligned}
\frac{\sin z}{\cos z} & =\left(z-\frac{z^3}{3 !}+\frac{z^5}{5 !}+\mathcal{O}\left(z^7\right)\right)\left(1+\frac{1}{2} z^2+\frac{5}{24} z^4+\mathcal{O}\left(z^6\right)\right) \\
& =z+\frac{1}{3} z^3+\frac{2}{15} z^5+\mathcal{O}\left(z^7\right) .
\end{aligned}
\]
The end result can be checked by differentiating $\tan z$ five times.
Note that $\tan z$ is an odd function, so that only odd terms appear in the power series.
:::
