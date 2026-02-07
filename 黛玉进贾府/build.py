#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build script to generate the complete HTML file."""
import os

html_content = r'''PLACEHOLDER'''

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '黛玉进贾府.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f"Written to {output_path}")
