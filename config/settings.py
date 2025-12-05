import fairdm

# Set up FairDM with the discussions plugin
fairdm.setup(
    apps=["fairdm_demo"],
    addons=["fairdm_discussions"],
)

# Set ROOT_URLCONF
ROOT_URLCONF = "fairdm.conf.urls"
