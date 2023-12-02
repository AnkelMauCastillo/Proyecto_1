<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="xml" version="1.0" indent="yes"/>
  <xsl:preserve-space elements="*"/>
  
  <xsl:template match="/">
    <libros>
      <!-- Iteración por cada objeto -->
      <xsl:for-each select="/django-objects/object">
        <libro>
          <!-- Iterar por cada elemento para extraer los tags XML y sus valores -->
          <xsl:for-each select="field">
            <xsl:element name="{@name}">
              <xsl:value-of select="."/>
            </xsl:element>
          </xsl:for-each>
        </libro>
      </xsl:for-each>
    </libros>
  </xsl:template>
</xsl:stylesheet>
