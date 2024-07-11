const express = require("express");
const { asyncHandler } = require("../../utils");

const router = express.Router();
const db = require("../../db/models");
const { where } = require("sequelize");

const { Tweet } = db;

router.get(
  "/",
  asyncHandler(async (req, res) => {
    const tweets = await Tweet.findAll();
    res.json(tweets);
  })
);

// added this route to delete a tweet
router.delete(
  "/:id",
  asyncHandler(async (req, res) => {
    console.log("req.params.id", req.params.id);
    const tweets = await Tweet.destroy({ where: { id: req.params.id } });
    res.json({ message: "Successfully deleted" });
  })
);

router.post(
  "",
  asyncHandler(async (req, res) => {
    const tweets = await Tweet.create(req.body);
    res.json(tweets);
  })
);

module.exports = router;
