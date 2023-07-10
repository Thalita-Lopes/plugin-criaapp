# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CriaAPP
                                 A QGIS plugin
 Este plugin cria APP
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-26
        copyright            : (C) 2023 by Thalita Mascarenhas
        email                : thalitamascarenhas@ufpr.br
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CriaAPP class from file CriaAPP.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .CriaAPP import CriaAPP
    return CriaAPP(iface)
