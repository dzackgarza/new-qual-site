---
schema: qual/card@1
id: P-BZIXT
kind: problem
title: "1. Parts:"
classification:
  areas: []
  topics: []
relations: []
review: draft
---
1. Parts:
   1. Let $x, y \in X$ and suppose $f(x) = f(y)$. By assumption, $g(f(x)) = x$ and $g(f(y)) = y$, and since we also have $g(f(x)) = g(f(y))$ we have $g(f(y)) = x$. But $g(f(y)) = y$, so $y=x$.
   2. Let $y\in Y$, we will find an $x\in X$ such that $g(x) = y$. We can consider $f(y)$, so let $x = f(y)$. We have $g(f(y)) = y$ by assumption, so $g(x) = g(f(y)) = y$ as desired.
   3. We need to have $f$ fail surjectivity and $g$ fail injectivity, so take $X = [1],~ Y = [2]$ where
   $$
   f(1) = 1, \\ 
   g(1) = 1, ~g(2) = 1
   $$
   ![](../../assets/00_Prelims/figures/2019-07-13-22-08-59.png)
   then $g(f(1)) = 1$, and this exhausts $X$. Since $\abs{X} \neq \abs{Y}$, these don't form a bijection -- in particular, $2\not\in\im f \subsetneq Y$.




