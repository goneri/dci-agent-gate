#!/usr/bin/python
import shade

shade.simple_logging(debug=True)
cloud = shade.openstack_cloud(cloud='defaults')
print(cloud.get_flavor_by_ram(512))
