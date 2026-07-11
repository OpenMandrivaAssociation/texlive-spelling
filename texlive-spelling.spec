%global tl_name spelling
%global tl_revision 73571

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.41
Release:	%{tl_revision}.1
Summary:	Support for spell-checking of LuaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/spelling
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spelling.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spelling.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package aids spell-checking of TeX documents compiled with the
LuaTeX engine. It can give visual feedback in PDF output similar to
WYSIWYG word processors. The package relies on an external spell-checker
application to check spelling of a text file and to output a list of bad
spellings. The package should work with most spell-checkers, even dumb,
TeX-unaware ones.

