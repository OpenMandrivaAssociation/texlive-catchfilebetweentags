%global tl_name catchfilebetweentags
%global tl_revision 21476

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Catch text delimited by docstrip tags
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/catchfilebetweentags
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/catchfilebetweentags.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/catchfilebetweentags.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/catchfilebetweentags.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package (built using the facilities of catchfile) provides a macro
\catchfilebetweentags acts like the original \catchfile but only
extracts a portion of the file instead of the complete file. The
extracted portion can be delimited by strings or by docstrip tags:
%<*tag> .... %</tag> (comments in the caught region may be included or
dropped).

