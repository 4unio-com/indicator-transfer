/*
 * Copyright 2014 Canonical Ltd.
 *
 * This program is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License version 3, as published
 * by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranties of
 * MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
 * PURPOSE.  See the GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Authors:
 *   Charles Kerr <charles.kerr@canonical.com>
 */

#ifndef INDICATOR_TRANSFER_VIEW_GMENU_H
#define INDICATOR_TRANSFER_VIEW_GMENU_H

#include <core/signal.h>

namespace unity {
namespace indicator {
namespace transfer {

/**
 * \brief a View that exports GActions and GMenus onto the DBus
 */
class GMenuView
{
public:
  GMenuView(const std::shared_ptr<const Model>& model,
            const std::shared_ptr<Controller>& controller);
  ~GMenuView();
  void set_controller(const std::shared_ptr<Controller>&);
  void set_model(const std::shared_ptr<Model>&);
  const core::Signal<>& name_lost() const;

private:
  class Impl;
  std::unique_ptr<Impl> p;
};

} // namespace transfer
} // namespace indicator
} // namespace unity

#endif // INDICATOR_TRANSFER_VIEW_GMENU_H
