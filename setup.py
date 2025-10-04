from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="516-digital-investigation-tools",
    version="1.0.0",
    author="516 Hackers",
    author_email="your-email@example.com",
    description="A comprehensive digital investigation and OSINT toolkit by 516 Hackers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'investigate516=scripts.sherlock_wrapper:main',
            'ig516=scripts.enhanced_instaloader:main',
            'meta516=scripts.metadata_analyzer:main',
            'image516=scripts.image_forensics:main',
            'social516=scripts.social_media_mapper:main',
            'email516=scripts.email_analyzer:main',
            'domain516=scripts.domain_research:main',
            'report516=scripts.report_generator:main',
        ],
    },
)
